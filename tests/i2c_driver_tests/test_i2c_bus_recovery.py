import pytest

from test_runner.fake_serial import FakeSerial
from tests.i2c_driver_tests.i2c_tester import I2CDriverTester


# verify i2c bus starts ready
@pytest.mark.i2c
def test_i2c_bus_ready():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)

    response = i2c.bus_status("I2C1")

    assert response == "OK I2C_BUS_READY I2C1"


# verify stuck i2c bus can be detected
@pytest.mark.i2c
def test_i2c_stuck_bus_detection():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)
    i2c.inject_stuck_bus("I2C1")

    response = i2c.bus_status("I2C1")

    assert response == "OK I2C_BUS_STUCK I2C1"


# verify stuck i2c bus can be recovered
@pytest.mark.i2c
def test_i2c_bus_recovery():

    device = FakeSerial()
    i2c = I2CDriverTester(device)

    i2c.configure("I2C1", 100000)
    i2c.inject_stuck_bus("I2C1")
    i2c.recover_bus("I2C1")

    response = i2c.bus_status("I2C1")

    assert response == "OK I2C_BUS_READY I2C1"