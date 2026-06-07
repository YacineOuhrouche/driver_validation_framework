from automation.gpio_regression_runner import run_gpio_regression


# verify gpio regression runner executes
def test_gpio_regression_runner_executes():

    code, stdout, stderr = run_gpio_regression()

    assert code == 0
    assert "passed" in stdout