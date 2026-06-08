from automation.uart_report_generator import generate_uart_report


# verify uart report file is generated
def test_uart_report_generator_creates_file():

    path, code = generate_uart_report()

    assert code == 0
    assert path.exists()
    assert "uart validation report" in path.read_text()