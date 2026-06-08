# spi validation helper
class SPIDriverTester:

    # store device backend
    def __init__(self, device):
        self.device = device

    # configure spi as master
    def configure_master(
        self,
        spi: str,
        cpol: int,
        cpha: int
    ) -> str:

        return self.device.send_command(
            f"SPI_CONFIG {spi} MASTER {cpol} {cpha}"
        )

    # configure spi as slave
    def configure_slave(
        self,
        spi: str,
        cpol: int,
        cpha: int
    ) -> str:

        return self.device.send_command(
            f"SPI_CONFIG {spi} SLAVE {cpol} {cpha}"
        )

    # attach simulated spi device
    def attach_device(self, spi: str, device_id: str) -> str:
        return self.device.send_command(
            f"SPI_ATTACH_DEVICE {spi} {device_id}"
        )

    # transfer spi data
    def transfer(
        self,
        spi: str,
        device_id: str,
        data: str
    ) -> str:

        return self.device.send_command(
            f"SPI_TRANSFER {spi} {device_id} {data}"
        )