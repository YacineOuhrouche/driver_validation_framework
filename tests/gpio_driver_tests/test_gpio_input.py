import pytest

from test_runner.fake_serial import FakeSerial
from tests.gpio_driver_tests.gpio_tester import GPIODriverTester


# Verify GPIO input configuration.
@pytest.mark.gpio
def test_gpio_configure_input():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    response = gpio.configure_input("PA5")

    assert response == "OK GPIO_CONFIG PA5 INPUT"


# Verify GPIO input reads HIGH.
@pytest.mark.gpio
def test_gpio_input_read_high():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")
    gpio.set_input_high("PA5")

    response = gpio.read("PA5")

    assert response == "OK GPIO_READ PA5 HIGH"


# Verify GPIO input reads LOW.
@pytest.mark.gpio
def test_gpio_input_read_low():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")
    gpio.set_input_low("PA5")

    response = gpio.read("PA5")

    assert response == "OK GPIO_READ PA5 LOW"


# Verify output write fails on input pin.
@pytest.mark.gpio
def test_gpio_write_to_input_pin_fails():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    response = gpio.write_high("PA5")

    assert response == "ERROR PIN_NOT_OUTPUT"


# Verify setting input fails on output pin.
@pytest.mark.gpio
def test_gpio_set_input_on_output_pin_fails():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_output("PA5")

    response = gpio.set_input_high("PA5")

    assert response == "ERROR PIN_NOT_INPUT"