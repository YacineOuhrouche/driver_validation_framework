from automation.regression_runner import run_dma_regression


# allow file to run directly
if __name__ == "__main__":

    code, stdout, stderr = run_dma_regression()

    print(stdout)

    if stderr:
        print(stderr)

    raise SystemExit(code)