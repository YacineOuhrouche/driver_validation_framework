import subprocess


# run pytest tests for a selected marker
def run_marked_regression(marker: str):

    result = subprocess.run(
        ["pytest", "-m", marker],
        capture_output=True,
        text=True
    )

    return result.returncode, result.stdout, result.stderr


# run gpio regression tests
def run_gpio_regression():

    return run_marked_regression("gpio")


# run uart regression tests
def run_uart_regression():

    return run_marked_regression("uart")


# allow file to run directly
if __name__ == "__main__":

    code, stdout, stderr = run_uart_regression()

    print(stdout)

    if stderr:
        print(stderr)

    raise SystemExit(code)