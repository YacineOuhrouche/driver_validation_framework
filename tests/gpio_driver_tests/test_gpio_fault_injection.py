import pytest

from test_runner.fake_serial import FakeSerial
from tests.gpio_driver_tests.gpio_tester import (
    GPIODriverTester
)
from fault_injection.gpio_fault_injector import (
    GPIOFaultInjector
)


# verify invalid mode fault
@pytest.mark.gpio
def test_fault_invalid_mode():

    device = FakeSerial()

    injector = GPIOFaultInjector(device)

    response = injector.invalid_mode()

    assert response == "ERROR INVALID_MODE"


# verify invalid state fault
@pytest.mark.gpio
def test_fault_invalid_state():

    device = FakeSerial()

    gpio = GPIODriverTester(device)

    gpio.configure_output("PA5")

    injector = GPIOFaultInjector(device)

    response = injector.invalid_state()

    assert response == "ERROR INVALID_STATE"


# verify invalid pull fault
@pytest.mark.gpio
def test_fault_invalid_pull():

    device = FakeSerial()

    gpio = GPIODriverTester(device)

    gpio.configure_input("PA5")

    injector = GPIOFaultInjector(device)

    response = injector.invalid_pull()

    assert response == "ERROR INVALID_PULL"


# verify unknown command fault
@pytest.mark.gpio
def test_fault_unknown_command():

    device = FakeSerial()

    injector = GPIOFaultInjector(device)

    response = injector.unknown_command()

    assert response == "ERROR UNKNOWN_COMMAND"