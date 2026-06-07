

#GPIO validation commands for a device
class GPIODriverTester:
   
    # store device communication backend
    def __init__(self, device):
        self.device = device

    # config a gpio pin as out
    def configure_output(self, pin: str) -> str:
        return self.device.send_command(f"GPIO_CONFIG {pin} OUTPUT")

    # set gpio as high
    def write_high(self, pin: str) -> str:
        return self.device.send_command(f"GPIO_WRITE {pin} HIGH")

    # idem for low
    def write_low(self, pin: str) -> str:
        return self.device.send_command(f"GPIO_WRITE {pin} LOW")

    # read a gpio pin state
    def read(self, pin: str) -> str:
        return self.device.send_command(f"GPIO_READ {pin}")