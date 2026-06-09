import pytest

from test_runner.fake_serial import FakeSerial
from tests.dma_driver_tests.dma_tester import DMADriverTester


# verify dma start fails before configuration
@pytest.mark.dma
def test_dma_start_without_config():

    device = FakeSerial()
    dma = DMADriverTester(device)

    response = dma.start_transfer(
        "DMA1_CH1",
        "SRC_BUF",
        "DST_BUF"
    )

    assert response == "ERROR DMA_NOT_CONFIGURED"


# verify dma complete fails without active transfer
@pytest.mark.dma
def test_dma_complete_without_active_transfer():

    device = FakeSerial()
    dma = DMADriverTester(device)

    response = dma.complete_transfer("DMA1_CH1")

    assert response == "ERROR DMA_TRANSFER_NOT_ACTIVE"


# verify dma idle status before transfer
@pytest.mark.dma
def test_dma_idle_status():

    device = FakeSerial()
    dma = DMADriverTester(device)

    response = dma.status("DMA1_CH1")

    assert response == "OK DMA_IDLE DMA1_CH1"


# verify no dma interrupt before completion
@pytest.mark.dma
def test_dma_no_interrupt():

    device = FakeSerial()
    dma = DMADriverTester(device)

    dma.configure("DMA1_CH1")

    response = dma.interrupt_status("DMA1_CH1")

    assert response == "OK DMA_NO_INTERRUPT DMA1_CH1"