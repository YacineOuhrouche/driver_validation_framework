import pytest

from test_runner.fake_serial import FakeSerial
from tests.spi_driver_tests.spi_tester import SPIDriverTester


# verify invalid spi role is rejected
@pytest.mark.spi
def test_spi_invalid_role():

    device = FakeSerial()

    response = device.send_command(
        "SPI_CONFIG SPI1 BADROLE 0 0"
    )

    assert response == "ERROR INVALID_SPI_ROLE"


# verify invalid cpol is rejected
@pytest.mark.spi
def test_spi_invalid_cpol():

    device = FakeSerial()

    response = device.send_command(
        "SPI_CONFIG SPI1 MASTER 2 0"
    )

    assert response == "ERROR INVALID_CPOL"


# verify invalid cpha is rejected
@pytest.mark.spi
def test_spi_invalid_cpha():

    device = FakeSerial()

    response = device.send_command(
        "SPI_CONFIG SPI1 MASTER 0 2"
    )

    assert response == "ERROR INVALID_CPHA"


# verify transfer fails before spi configuration
@pytest.mark.spi
def test_spi_transfer_without_config():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    response = spi.transfer("SPI1", "DEV1", "A5")

    assert response == "ERROR SPI_NOT_CONFIGURED"


# verify attach device fails before spi configuration
@pytest.mark.spi
def test_spi_attach_without_config():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    response = spi.attach_device("SPI1", "DEV1")

    assert response == "ERROR SPI_NOT_CONFIGURED"


# verify transfer fails when device is missing
@pytest.mark.spi
def test_spi_transfer_missing_device():

    device = FakeSerial()
    spi = SPIDriverTester(device)

    spi.configure_master("SPI1", 0, 0)

    response = spi.transfer("SPI1", "DEV1", "A5")

    assert response == "ERROR SPI_DEVICE_NOT_FOUND"