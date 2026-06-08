from datetime import datetime
from pathlib import Path

from automation.regression_runner import run_uart_regression


# generate uart validation report
def generate_uart_report():

    code, stdout, stderr = run_uart_regression()

    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    report_path = report_dir / f"uart_validation_report_{timestamp}.txt"

    report_content = f"""
uart validation report
======================

timestamp: {timestamp}
result: {"pass" if code == 0 else "fail"}

pytest output:
--------------
{stdout}

pytest errors:
--------------
{stderr}
"""

    report_path.write_text(report_content)

    return report_path, code


# allow file to run directly
if __name__ == "__main__":

    path, code = generate_uart_report()

    print(f"report generated: {path}")

    raise SystemExit(code)