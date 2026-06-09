import pytest

from test_runner.fake_serial import FakeSerial
from tests.spi_driver_tests.spi_tester import SPIDriverTester


# verify multiple spi devices can attach to same bus
@pytest.mark.spi
def test_spi_attach_multiple_devices():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    spi.configure_master("SPI1", 0, 0)

    response_1 = spi.attach_device("SPI1", "DEV1")
    response_2 = spi.attach_device("SPI1", "DEV2")

    assert response_1 == "OK SPI_ATTACH_DEVICE SPI1 DEV1"
    assert response_2 == "OK SPI_ATTACH_DEVICE SPI1 DEV2"


# verify transfer to first spi device
@pytest.mark.spi
def test_spi_transfer_to_device_1():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    spi.configure_master("SPI1", 0, 0)
    spi.attach_device("SPI1", "DEV1")
    spi.attach_device("SPI1", "DEV2")

    response = spi.transfer("SPI1", "DEV1", "A5")

    assert response == "OK SPI_TRANSFER SPI1 DEV1 A5"


# verify transfer to second spi device
@pytest.mark.spi
def test_spi_transfer_to_device_2():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    spi.configure_master("SPI1", 0, 0)
    spi.attach_device("SPI1", "DEV1")
    spi.attach_device("SPI1", "DEV2")

    response = spi.transfer("SPI1", "DEV2", "5A")

    assert response == "OK SPI_TRANSFER SPI1 DEV2 5A"


# verify device bus mismatch is detected
@pytest.mark.spi
def test_spi_device_bus_mismatch():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    spi.configure_master("SPI1", 0, 0)
    spi.configure_master("SPI2", 0, 0)

    spi.attach_device("SPI1", "DEV1")

    response = spi.transfer("SPI2", "DEV1", "A5")

    assert response == "ERROR SPI_DEVICE_BUS_MISMATCH"