import pytest

from test_runner.fake_serial import FakeSerial
from tests.spi_driver_tests.spi_tester import SPIDriverTester


# verify spi master configuration
@pytest.mark.spi
def test_spi_configure_master():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    response = spi.configure_master("SPI1", 0, 0)

    assert response == "OK SPI_CONFIG SPI1 MASTER CPOL0 CPHA0"


# verify spi slave configuration
@pytest.mark.spi
def test_spi_configure_slave():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    response = spi.configure_slave("SPI1", 0, 0)

    assert response == "OK SPI_CONFIG SPI1 SLAVE CPOL0 CPHA0"


# verify spi device attachment
@pytest.mark.spi
def test_spi_attach_device():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    spi.configure_master("SPI1", 0, 0)

    response = spi.attach_device("SPI1", "DEV1")

    assert response == "OK SPI_ATTACH_DEVICE SPI1 DEV1"


# verify spi transfer integrity
@pytest.mark.spi
def test_spi_transfer_data():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    spi.configure_master("SPI1", 0, 0)
    spi.attach_device("SPI1", "DEV1")

    response = spi.transfer("SPI1", "DEV1", "A5")

    assert response == "OK SPI_TRANSFER SPI1 DEV1 A5"