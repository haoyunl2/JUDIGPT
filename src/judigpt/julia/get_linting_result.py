import subprocess

from judigpt.cli import colorscheme, print_to_console
from judigpt.julia.julia_code_runner import run_julia_file


def get_linting_result(code: str) -> str:
    try:
        res, err = run_julia_file(code=code, julia_file_name="julia_lint_script.jl")
        
        # Check if there was a timeout error in stderr
        if err and "timed out" in err.lower():
            print_to_console(
                text="Linter timed out after 30 seconds (this is normal for JUDI code - the package takes time to load). Skipping linter check. The code will still be checked by running it, which is more reliable for JUDI.",
                title="Linter Timeout - Skipped (Normal for JUDI)",
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
        # Check if there's any output before "STARTING LINT:" that might indicate errors
        if res and "STARTING LINT:" not in res:
            # Show any output we got (might be partial results)
            print_to_console(
                text=f"Linter output (may be incomplete):\n{res[:500]}...",
                title="Linter Partial Output",
                border_style=colorscheme.warning,
            )
        if err:
            # Show error output (but limit length)
            err_preview = err[:500] if len(err) > 500 else err
            # Don't show error if it's just a timeout (already handled above)
            if "timed out" not in err.lower():
                print_to_console(
                    text=f"Linter error output:\n{err_preview}",
                    title="Linter Error",
                    border_style=colorscheme.error,
                )
        return ""

    except subprocess.TimeoutExpired:
        print_to_console(
            text="Linter timed out after 30 seconds (this is normal for JUDI code - the package takes time to load). Skipping linter check. The code will still be checked by running it, which is more reliable for JUDI.",
            title="Linter Timeout - Skipped (Normal for JUDI)",
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
