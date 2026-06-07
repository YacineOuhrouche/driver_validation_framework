import pytest

from test_runner.fake_serial import FakeSerial
from tests.uart_driver_tests.uart_tester import UARTDriverTester


# verify uart framing error is detected
@pytest.mark.uart
def test_uart_framing_error_detection():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    uart.configure("UART1", 115200)
    uart.inject_framing_error("UART1")

    response = uart.error_status("UART1")

    assert response == "OK UART_ERROR UART1 FRAMING"


# verify uart error status clears after read
@pytest.mark.uart
def test_uart_error_status_clears_after_read():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    uart.configure("UART1", 115200)
    uart.inject_framing_error("UART1")

    uart.error_status("UART1")

    response = uart.error_status("UART1")

    assert response == "OK UART_NO_ERROR UART1"