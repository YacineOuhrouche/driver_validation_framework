import pytest

from test_runner.fake_serial import FakeSerial
from tests.i2c_driver_tests.i2c_tester import I2CDriverTester


# verify invalid i2c speed is rejected
@pytest.mark.i2c
def test_i2c_invalid_speed():

    device = FakeSerial()

    response = device.send_command(
        "I2C_CONFIG I2C1 12345"
    )

    assert response == "ERROR INVALID_I2C_SPEED"


# verify attach fails before i2c configuration
@pytest.mark.i2c
def test_i2c_attach_without_config():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    response = i2c.attach_device("I2C1", "0x48")

    assert response == "ERROR I2C_NOT_CONFIGURED"


# verify write fails before i2c configuration
@pytest.mark.i2c
def test_i2c_write_without_config():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    response = i2c.write("I2C1", "0x48", "A5")

    assert response == "ERROR I2C_NOT_CONFIGURED"


# verify read fails before i2c configuration
@pytest.mark.i2c
def test_i2c_read_without_config():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    response = i2c.read("I2C1", "0x48")

    assert response == "ERROR I2C_NOT_CONFIGURED"


# verify nack when device address is missing
@pytest.mark.i2c
def test_i2c_write_missing_device_nack():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)

    response = i2c.write("I2C1", "0x48", "A5")

    assert response == "ERROR I2C_NACK"


# verify read nack when device address is missing
@pytest.mark.i2c
def test_i2c_read_missing_device_nack():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)

    response = i2c.read("I2C1", "0x48")

    assert response == "ERROR I2C_NACK"


# verify i2c bus mismatch is detected
@pytest.mark.i2c
def test_i2c_bus_mismatch():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)
    i2c.configure("I2C2", 100000)

    i2c.attach_device("I2C1", "0x48")

    response = i2c.write("I2C2", "0x48", "A5")

    assert response == "ERROR I2C_BUS_MISMATCH"