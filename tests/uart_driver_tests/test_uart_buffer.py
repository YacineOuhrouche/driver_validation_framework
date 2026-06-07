import pytest

from test_runner.fake_serial import FakeSerial
from tests.uart_driver_tests.uart_tester import UARTDriverTester


# verify uart rx buffer overflow is detected
@pytest.mark.uart
def test_uart_rx_buffer_overflow():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    uart.configure("UART1", 115200)

    uart.inject_rx("UART1", "A")
    uart.inject_rx("UART1", "B")
    uart.inject_rx("UART1", "C")

    response = uart.inject_rx("UART1", "D")

    assert response == "ERROR UART_RX_OVERFLOW UART1"


# verify uart receive timeout when buffer is empty
@pytest.mark.uart
def test_uart_receive_timeout_behavior():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    uart.configure("UART1", 115200)

    response = uart.receive("UART1")

    assert response == "OK UART_RX_EMPTY UART1"