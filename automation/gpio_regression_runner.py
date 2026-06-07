import subprocess


# run all gpio pytest tests
def run_gpio_regression():

    result = subprocess.run(
        ["pytest", "-m", "gpio"],
        capture_output=True,
        text=True
    )

    return result.returncode, result.stdout, result.stderr


# allow file to run directly
if __name__ == "__main__":

    code, stdout, stderr = run_gpio_regression()

    print(stdout)

    if stderr:
        print(stderr)

    raise SystemExit(code)