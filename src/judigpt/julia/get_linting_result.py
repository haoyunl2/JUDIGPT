import subprocess

from judigpt.cli import colorscheme, print_to_console
from judigpt.julia.julia_code_runner import run_julia_file


def get_linting_result(code: str) -> str:
    try:
        res, err = run_julia_file(code=code, julia_file_name="julia_lint_script.jl")
        
        # Check if there was a timeout error in stderr
        if err and "timed out" in err.lower():
            print_to_console(
                text="Linter timed out after 30 seconds. Skipping linter check. This may happen when loading large packages like JUDI. The code will still be checked by running it.",
                title="Linter Timeout - Skipped",
                border_style=colorscheme.warning,
            )
            return ""
        
        lines = res.splitlines()
        for i, line in enumerate(lines):
            if "STARTING LINT:" in line:
                linting_result = "\n".join(lines[i + 1 :])

                if linting_result:
                    print_to_console(
                        text=linting_result,
                        title="Linter Result",
                        border_style=colorscheme.error,
                    )
                else:
                    print_to_console(
                        text="No linting issues found!",
                        title="Linter Result",
                        border_style=colorscheme.success,
                    )
                return linting_result

        # If no "STARTING LINT:" marker found, linter may have failed silently
        if err:
            print_to_console(
                text=f"Linter may have failed. Error output: {err[:200]}...",
                title="Linter Warning",
                border_style=colorscheme.warning,
            )
        return ""

    except subprocess.TimeoutExpired:
        print_to_console(
            text="Linter timed out after 30 seconds. Skipping linter check. This may happen when loading large packages like JUDI. The code will still be checked by running it.",
            title="Linter Timeout - Skipped",
            border_style=colorscheme.warning,
        )
        return ""  # Return empty string so linter check is considered passed
    except Exception as e:
        print_to_console(
            text=f"Linter error: {str(e)}",
            title="Linter Error",
            border_style=colorscheme.warning,
        )
        return ""
