from automation.regression_runner import run_spi_regression


# allow file to run directly
if __name__ == "__main__":

    code, stdout, stderr = run_spi_regression()

    print(stdout)

    if stderr:
        print(stderr)

    raise SystemExit(code)