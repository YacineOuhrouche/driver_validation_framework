import pytest

from test_runner.fake_serial import FakeSerial
from tests.dma_driver_tests.dma_tester import DMADriverTester


# verify dma channel configuration
@pytest.mark.dma
def test_dma_configure_channel():

    device = FakeSerial()
    dma = DMADriverTester(device)

    response = dma.configure("DMA1_CH1")

    assert response == "OK DMA_CONFIG DMA1_CH1"


# verify dma transfer start
@pytest.mark.dma
def test_dma_start_transfer():

    device = FakeSerial()
    dma = DMADriverTester(device)

    dma.configure("DMA1_CH1")

    response = dma.start_transfer(
        "DMA1_CH1",
        "SRC_BUF",
        "DST_BUF"
    )

    assert response == "OK DMA_START DMA1_CH1 SRC_BUF DST_BUF"


# verify dma active status
@pytest.mark.dma
def test_dma_active_status():

    device = FakeSerial()
    dma = DMADriverTester(device)

    dma.configure("DMA1_CH1")
    dma.start_transfer("DMA1_CH1", "SRC_BUF", "DST_BUF")

    response = dma.status("DMA1_CH1")

    assert response == "OK DMA_STATUS DMA1_CH1 ACTIVE"


# verify dma transfer completion
@pytest.mark.dma
def test_dma_complete_transfer():

    device = FakeSerial()
    dma = DMADriverTester(device)

    dma.configure("DMA1_CH1")
    dma.start_transfer("DMA1_CH1", "SRC_BUF", "DST_BUF")

    response = dma.complete_transfer("DMA1_CH1")

    assert response == "OK DMA_COMPLETE DMA1_CH1"


# verify dma complete status
@pytest.mark.dma
def test_dma_complete_status():

    device = FakeSerial()
    dma = DMADriverTester(device)

    dma.configure("DMA1_CH1")
    dma.start_transfer("DMA1_CH1", "SRC_BUF", "DST_BUF")
    dma.complete_transfer("DMA1_CH1")

    response = dma.status("DMA1_CH1")

    assert response == "OK DMA_STATUS DMA1_CH1 COMPLETE"


# verify dma completion interrupt
@pytest.mark.dma
def test_dma_completion_interrupt():

    device = FakeSerial()
    dma = DMADriverTester(device)

    dma.configure("DMA1_CH1")
    dma.start_transfer("DMA1_CH1", "SRC_BUF", "DST_BUF")
    dma.complete_transfer("DMA1_CH1")

    response = dma.interrupt_status("DMA1_CH1")

    assert response == "OK DMA_INTERRUPT DMA1_CH1"