from automation.gpio_report_generator import generate_gpio_report


# verify gpio report file is generated
def test_gpio_report_generator_creates_file():

    path, code = generate_gpio_report()

    assert code == 0
    assert path.exists()
    assert "gpio validation report" in path.read_text()