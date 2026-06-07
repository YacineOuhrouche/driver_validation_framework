import pytest

from test_runner.fake_serial import FakeSerial
from tests.gpio_driver_tests.gpio_tester import (
    GPIODriverTester
)


# Verify rising edge interrupt.
@pytest.mark.gpio
def test_rising_edge_interrupt():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    gpio.configure_rising_interrupt("PA5")

    gpio.set_input_low("PA5")
    gpio.set_input_high("PA5")

    response = gpio.interrupt_status("PA5")

    assert response == "OK GPIO_INTERRUPT PA5"


# Verify falling edge interrupt.
@pytest.mark.gpio
def test_falling_edge_interrupt():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    gpio.set_input_high("PA5")

    gpio.configure_falling_interrupt("PA5")

    gpio.set_input_low("PA5")

    response = gpio.interrupt_status("PA5")

    assert response == "OK GPIO_INTERRUPT PA5"


# Verify no interrupt occurred.
@pytest.mark.gpio
def test_no_interrupt():

    device = FakeSerial()
    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    response = gpio.interrupt_status("PA5")

    assert response == "OK GPIO_NO_INTERRUPT PA5"