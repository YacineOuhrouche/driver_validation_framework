import pytest

from test_runner.fake_serial import FakeSerial
from tests.i2c_driver_tests.i2c_tester import I2CDriverTester


# verify i2c standard speed configuration
@pytest.mark.i2c
def test_i2c_configure_standard_speed():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    response = i2c.configure("I2C1", 100000)

    assert response == "OK I2C_CONFIG I2C1 100000"


# verify i2c fast speed configuration
@pytest.mark.i2c
def test_i2c_configure_fast_speed():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    response = i2c.configure("I2C1", 400000)

    assert response == "OK I2C_CONFIG I2C1 400000"


# verify i2c device attachment
@pytest.mark.i2c
def test_i2c_attach_device():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)

    response = i2c.attach_device("I2C1", "0x48")

    assert response == "OK I2C_ATTACH_DEVICE I2C1 0x48"


# verify i2c write operation
@pytest.mark.i2c
def test_i2c_write_data():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)
    i2c.attach_device("I2C1", "0x48")

    response = i2c.write("I2C1", "0x48", "A5")

    assert response == "OK I2C_WRITE I2C1 0x48 A5"


# verify i2c read operation
@pytest.mark.i2c
def test_i2c_read_data():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)
    i2c.attach_device("I2C1", "0x48")
    i2c.write("I2C1", "0x48", "A5")

    response = i2c.read("I2C1", "0x48")

    assert response == "OK I2C_READ I2C1 0x48 A5"


# verify empty i2c read
@pytest.mark.i2c
def test_i2c_read_empty():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)
    i2c.attach_device("I2C1", "0x48")

    response = i2c.read("I2C1", "0x48")

    assert response == "OK I2C_READ_EMPTY I2C1 0x48"