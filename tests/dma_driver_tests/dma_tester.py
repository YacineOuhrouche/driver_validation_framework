# dma validation helper
class DMADriverTester:

    # store device backend
    def __init__(self, device):
        self.device = device

    # configure dma channel
    def configure(self, channel: str) -> str:
        return self.device.send_command(
            f"DMA_CONFIG {channel}"
        )

    # start dma transfer
    def start_transfer(
        self,
        channel: str,
        source: str,
        destination: str
    ) -> str:

        return self.device.send_command(
            f"DMA_START {channel} {source} {destination}"
        )

    # complete dma transfer
    def complete_transfer(self, channel: str) -> str:
        return self.device.send_command(
            f"DMA_COMPLETE {channel}"
        )

    # read dma transfer status
    def status(self, channel: str) -> str:
        return self.device.send_command(
            f"DMA_STATUS {channel}"
        )

    # read dma interrupt status
    def interrupt_status(self, channel: str) -> str:
        return self.device.send_command(
            f"DMA_INTERRUPT_STATUS {channel}"
        )