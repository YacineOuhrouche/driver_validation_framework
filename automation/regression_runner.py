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


# run spi regression tests
def run_spi_regression():

    return run_marked_regression("spi")

# run i2c regression tests
def run_i2c_regression():

    return run_marked_regression("i2c")