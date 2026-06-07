import pytest

from test_runner.fake_serial import FakeSerial
from tests.gpio_driver_tests.gpio_tester import GPIODriverTester


# Verify GPIO output configuration.
@pytest.mark.gpio
def test_gpio_configure_output():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    response = gpio.configure_output("PA5")

    assert response == "OK GPIO_CONFIG PA5 OUTPUT"


# Verify GPIO can be driven HIGH.
@pytest.mark.gpio
def test_gpio_write_high():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_output("PA5")

    response = gpio.write_high("PA5")

    assert response == "OK GPIO_WRITE PA5 HIGH"


# Verify GPIO can be driven LOW.
@pytest.mark.gpio
def test_gpio_write_low():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_output("PA5")

    response = gpio.write_low("PA5")

    assert response == "OK GPIO_WRITE PA5 LOW"


# Verify GPIO readback after HIGH write.
@pytest.mark.gpio
def test_gpio_read_after_write_high():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_output("PA5")
    gpio.write_high("PA5")

    response = gpio.read("PA5")

    assert response == "OK GPIO_READ PA5 HIGH"


# Verify GPIO readback after LOW write.
@pytest.mark.gpio
def test_gpio_read_after_write_low():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_output("PA5")
    gpio.write_low("PA5")

    response = gpio.read("PA5")

    assert response == "OK GPIO_READ PA5 LOW"