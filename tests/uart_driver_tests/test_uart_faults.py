import pytest

from test_runner.fake_serial import FakeSerial
from tests.uart_driver_tests.uart_tester import UARTDriverTester


# verify invalid baud rate is rejected
@pytest.mark.uart
def test_uart_invalid_baud_rate():

    device = FakeSerial()

    response = device.send_command("UART_CONFIG UART1 FAST")

    assert response == "ERROR INVALID_BAUD"


# verify transmit fails before uart configuration
@pytest.mark.uart
def test_uart_tx_without_config():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    response = uart.transmit("UART1", "HELLO")

    assert response == "ERROR UART_NOT_CONFIGURED"


# verify receive fails before uart configuration
@pytest.mark.uart
def test_uart_rx_without_config():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    response = uart.receive("UART1")

    assert response == "ERROR UART_NOT_CONFIGURED"


# verify rx injection fails before uart configuration
@pytest.mark.uart
def test_uart_inject_rx_without_config():

    device = FakeSerial()
    uart = UARTDriverTester(device)

    response = uart.inject_rx("UART1", "HELLO")

    assert response == "ERROR UART_NOT_CONFIGURED"