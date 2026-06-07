import pytest

from test_runner.fake_serial import FakeSerial
from tests.gpio_driver_tests.gpio_tester import GPIODriverTester


# Verify pull-up makes floating input read HIGH.
@pytest.mark.gpio
def test_gpio_pull_up_reads_high():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    response = gpio.enable_pull_up("PA5")
    readback = gpio.read("PA5")

    assert response == "OK GPIO_PULL PA5 UP"
    assert readback == "OK GPIO_READ PA5 HIGH"


# Verify pull-down makes floating input read LOW.
@pytest.mark.gpio
def test_gpio_pull_down_reads_low():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    response = gpio.enable_pull_down("PA5")
    readback = gpio.read("PA5")

    assert response == "OK GPIO_PULL PA5 DOWN"
    assert readback == "OK GPIO_READ PA5 LOW"


# Verify pull configuration fails on output pin.
@pytest.mark.gpio
def test_gpio_pull_on_output_pin_fails():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_output("PA5")

    response = gpio.enable_pull_up("PA5")

    assert response == "ERROR PIN_NOT_INPUT"


# Verify invalid pull setting is rejected.
@pytest.mark.gpio
def test_gpio_invalid_pull_setting():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    response = device.send_command("GPIO_PULL PA5 SIDEWAYS")

    assert response == "ERROR INVALID_PULL"