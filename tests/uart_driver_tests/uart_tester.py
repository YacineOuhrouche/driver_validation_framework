# uart validation helper
class UARTDriverTester:

    # store device backend
    def __init__(self, device):
        self.device = device

    # configure uart baud rate
    def configure(self, uart: str, baud: int) -> str:
        return self.device.send_command(
            f"UART_CONFIG {uart} {baud}"
        )

    # transmit uart data
    def transmit(self, uart: str, data: str) -> str:
        return self.device.send_command(
            f"UART_TX {uart} {data}"
        )

    # inject uart receive data
    def inject_rx(self, uart: str, data: str) -> str:
        return self.device.send_command(
            f"UART_INJECT_RX {uart} {data}"
        )

    # read uart received data
    def receive(self, uart: str) -> str:
        return self.device.send_command(
            f"UART_RX {uart}"
        )