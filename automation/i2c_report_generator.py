from datetime import datetime
from pathlib import Path

from automation.regression_runner import run_i2c_regression


# generate i2c validation report
def generate_i2c_report():

    code, stdout, stderr = run_i2c_regression()

    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    report_path = report_dir / f"i2c_validation_report_{timestamp}.txt"

    report_content = f"""
i2c validation report
=====================

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

    path, code = generate_i2c_report()

    print(f"report generated: {path}")

    raise SystemExit(code)