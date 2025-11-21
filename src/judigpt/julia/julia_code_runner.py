import os
import re
import subprocess
import tempfile
import time
from typing import Union


def run_julia_file(code: str, julia_file_name: str, project_dir: str | None = None):
    assert julia_file_name.endswith(".jl"), "julia_file_name must end with .jl"

    if project_dir is None:
        project_dir = os.getcwd()

    # Create a temporary file with Julia code in the project directory
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".jl", delete=False, encoding="utf-8", dir=project_dir
    ) as temp_file:
        temp_file.write(code)
        temp_file.flush()  # Ensure content is written to disk
        temp_file_path = temp_file.name

    try:
        # Run the Julia file with the project activated
        julia_script = os.path.join(
            project_dir, "src", "judigpt", "julia", julia_file_name
        )
        result = subprocess.run(
            [
                "julia",
                f"--project={project_dir}",
                julia_script,
                project_dir,
                temp_file_path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=project_dir,
            timeout=30,  # 30 second timeout for linting (reduced from 60)
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired as e:
        # Kill the process if it's still running
        try:
            process = getattr(e, 'process', None)
            if process is not None:
                process.kill()
        except:
            pass
        return "", "Error: Julia process timed out after 30 seconds. This may happen when loading large packages like JUDI. The linter check was skipped."
    finally:
        # Clean up the temporary file
        try:
            os.unlink(temp_file_path)
        except OSError:
            pass  # File might already be deleted


def run_code_string_direct(code: str, project_dir: str | None = None):
    """
    Alternative approach: Run Julia code directly using -e flag instead of temporary file.
    """
    if project_dir is None:
        project_dir = os.getcwd()

    try:
        result = subprocess.run(
            ["julia", f"--project={project_dir}", "-e", code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=project_dir,
            timeout=180,  # 180 second timeout for code execution (JUDI package loading can be slow)
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired as e:
        # Kill the process if it's still running
        try:
            process = getattr(e, 'process', None)
            if process is not None:
                process.kill()
        except:
            pass
        return "", "Error: Julia code execution timed out after 180 seconds. This may happen with complex simulations or when loading large packages."
    except Exception as e:
        return "", f"Error running Julia: {e}"


def _split_stacktrace(msg: str):
    """
    Split a Julia error message into the main error message and the stacktrace.

    Args:
        msg (str): The full error message string from Julia.

    Returns:
        tuple: (main error message, stacktrace) if found, otherwise (msg, None)
    """
    marker = "\nStacktrace:\n"
    if marker in msg:
        pre_stack, stack = msg.split(marker, 1)
        return pre_stack.strip(), stack.strip()
    else:
        # Handle the case where "Stacktrace" is part of the string but not split cleanly
        m = re.search(r"(.*?)(\nStacktrace:\n.*)", msg, re.DOTALL)
        if m:
            return m.group(1).strip(), m.group(2).replace("Stacktrace:\n", "").strip()
    return msg.strip(), None


def _filter_stacktrace(stack: str, exclude_patterns=None) -> Union[str, None]:
    """
    Filter out lines in a Julia stacktrace that are internal to PythonCall, JlWrap, or other irrelevant internals.

    Args:
        stack (str): The full stacktrace string from Julia.
        exclude_patterns (list, optional): List of regex patterns to exclude from the stacktrace.

    Returns:
        str or None: The filtered stacktrace, or None if all lines are excluded.
    """
    if exclude_patterns is None:
        exclude_patterns = [r"PythonCall", r"JlWrap", r"juliacall", r"pyjlmodule_seval"]

    lines = stack.splitlines()
    keep_lines = []
    for line in lines:
        if not any(re.search(pattern, line) for pattern in exclude_patterns):
            keep_lines.append(line)
    return "\n".join(keep_lines) if keep_lines else None


def get_error_message(result) -> str:
    """
    Format the error message and stacktrace from a result dictionary returned by run_string.

    Args:
        result (dict): The result dictionary from run_string.

    Returns:
        str: The formatted error message including stacktrace if available.
    """
    out_string = f"{result['error_message']}"
    if result["error_stacktrace"] is not None:
        out_string += f"\n\nStacktrace:\n{result['error_stacktrace']}"
    return out_string


def run_code(code: str) -> dict:
    start_time = time.time()
    stdout, stderr = run_code_string_direct(code=code)
    end_time = time.time()

    if stderr:
        # Check if stderr only contains CondaPkg initialization messages
        # These are normal and don't indicate actual errors
        condapkg_indicators = [
            "CondaPkg Found dependencies",
            "CondaPkg Initialising",
            "CondaPkg Installing packages",
            "The default environment has been installed",
            "Operator",
            "ran in",
        ]
        
        # Check if stderr is mostly CondaPkg messages
        stderr_lower = stderr.lower()
        is_mostly_condapkg = any(indicator.lower() in stderr_lower for indicator in condapkg_indicators)
        
        # Check for actual error indicators (not just CondaPkg noise)
        actual_error_indicators = [
            "error:",
            "exception:",
            "methoderror",
            "typeerror",
            "argumenterror",
            "loaderror",
            "stacktrace:",
        ]
        has_actual_error = any(
            indicator.lower() in stderr_lower for indicator in actual_error_indicators
        )
        
        # If stderr contains CondaPkg messages but no actual errors, treat as success
        if is_mostly_condapkg and not has_actual_error:
            # Check if there's a success indicator like "Operator ... ran"
            if "ran in" in stderr or "Operator" in stderr:
                result = {
                    "output": stdout,
                    "error": False,
                    "error_message": "",
                    "error_stacktrace": "",
                    "runtime": end_time - start_time,
                }
                return result
        
        # Otherwise, treat as error
        error_message, error_stacktrace = _split_stacktrace(stderr)

        result = {
            "output": stdout,
            "error": True,
            "error_message": error_message,
            "error_stacktrace": error_stacktrace,
            "runtime": end_time - start_time,
        }
        return result

    result = {
        "output": stdout,
        "error": False,
        "error_message": "",
        "error_stacktrace": "",
        "runtime": end_time - start_time,
    }
    return result
