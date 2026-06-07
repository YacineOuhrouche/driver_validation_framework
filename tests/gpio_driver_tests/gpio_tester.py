# GPIO validation helper.
class GPIODriverTester:

    # store device backend
    def __init__(self, device):
        self.device = device

    # configure GPIO output mode
    def configure_output(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_CONFIG {pin} OUTPUT"
        )

    # drive GPIO HIGH
    def write_high(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_WRITE {pin} HIGH"
        )

    # drive GPIO LOW
    def write_low(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_WRITE {pin} LOW"
        )

    # read GPIO state
    def read(self, pin: str) -> str:
        return self.device.send_command(
            f"GPIO_READ {pin}"
        )