# GPIO validation helper.
class GPIODriverTester:

    # Store device backend
    def __init__(self, device):
        self.device = device

    # Configure GPIO output mode
    def configure_output(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_CONFIG {pin} OUTPUT"
        )

    # Configure GPIO input mode
    def configure_input(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_CONFIG {pin} INPUT"
        )

    # Configure GPIO pull-up
    def enable_pull_up(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_PULL {pin} UP"
        )

    # Configure GPIO pull-down
    def enable_pull_down(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_PULL {pin} DOWN"
        )

    # Disable GPIO pull resistor
    def disable_pull(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_PULL {pin} NONE"
        )

    # Drive GPIO HIGH
    def write_high(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_WRITE {pin} HIGH"
        )

    # Drive GPIO LOW
    def write_low(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_WRITE {pin} LOW"
        )

    # Simulate external HIGH input
    def set_input_high(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_SET_INPUT {pin} HIGH"
        )

    # Simulate external LOW input
    def set_input_low(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_SET_INPUT {pin} LOW"
        )

    # Read GPIO state
    def read(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_READ {pin}"
        )