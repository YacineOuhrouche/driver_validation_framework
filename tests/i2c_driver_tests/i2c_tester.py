# i2c validation helper
class I2CDriverTester:

    # store device backend
    def __init__(self, device):
        self.device = device

    # configure i2c bus speed
    def configure(self, bus: str, speed: int) -> str:
        return self.device.send_command(
            f"I2C_CONFIG {bus} {speed}"
        )

    # attach simulated i2c device
    def attach_device(self, bus: str, address: str) -> str:
        return self.device.send_command(
            f"I2C_ATTACH_DEVICE {bus} {address}"
        )

    # write data to i2c device
    def write(self, bus: str, address: str, data: str) -> str:
        return self.device.send_command(
            f"I2C_WRITE {bus} {address} {data}"
        )

    # read data from i2c device
    def read(self, bus: str, address: str) -> str:
        return self.device.send_command(
            f"I2C_READ {bus} {address}"
        )

    # inject stuck bus fault
    def inject_stuck_bus(self, bus: str) -> str:
        return self.device.send_command(
            f"I2C_INJECT_STUCK_BUS {bus}"
        )

    # recover i2c bus
    def recover_bus(self, bus: str) -> str:
        return self.device.send_command(
            f"I2C_RECOVER_BUS {bus}"
        )

    # read i2c bus status
    def bus_status(self, bus: str) -> str:
        return self.device.send_command(
            f"I2C_BUS_STATUS {bus}"
        )