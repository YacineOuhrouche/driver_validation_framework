import pytest

from test_runner.fake_serial import FakeSerial
from tests.gpio_driver_tests.gpio_tester import GPIODriverTester

# verify that a gpio pin can be config as output
@pytest.mark.gpio
def test_gpio_configure_output():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    response = gpio.configure_output("PA5")

    assert response == "OK GPIO_CONFIG PA5 OUTPUT"


# verify that a gpio output pin can be driven
@pytest.mark.gpio
def test_gpio_write_high():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    response = gpio.write_high("PA5")

    assert response == "OK GPIO_WRITE PA5 HIGH"


@pytest.mark.gpio
def test_gpio_write_low():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    response = gpio.write_low("PA5")

    assert response == "OK GPIO_WRITE PA5 LOW"