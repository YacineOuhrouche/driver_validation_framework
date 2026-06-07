import pytest

from test_runner.fake_serial import FakeSerial
from tests.uart_driver_tests.uart_tester import UARTDriverTester


# verify uart baud configuration
@pytest.mark.uart
def test_uart_configure_baud_rate():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    response = uart.configure("UART1", 115200)

    assert response == "OK UART_CONFIG UART1 115200"


# verify uart transmission
@pytest.mark.uart
def test_uart_transmit_data():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    uart.configure("UART1", 115200)

    response = uart.transmit("UART1", "HELLO")

    assert response == "OK UART_TX UART1 HELLO"


# verify uart receive data
@pytest.mark.uart
def test_uart_receive_data():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    uart.configure("UART1", 115200)
    uart.inject_rx("UART1", "HELLO")

    response = uart.receive("UART1")

    assert response == "OK UART_RX UART1 HELLO"


# verify empty uart receive buffer
@pytest.mark.uart
def test_uart_receive_empty():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    uart.configure("UART1", 115200)

    response = uart.receive("UART1")

    assert response == "OK UART_RX_EMPTY UART1"