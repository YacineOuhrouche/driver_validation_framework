from test_runner.device_interface import DeviceInterface


# mock serial device 
class FakeSerial(DeviceInterface):

    # initialize simulated GPIO states
    def __init__(self):
        self.gpio_states = {}

    # open fake device connection
    def connect(self):
        pass

    # process commands and return simulated responses
    def send_command(self, command: str) -> str:

        parts = command.split()

        if command == "PING":
            return "OK PONG"

        if len(parts) == 3 and parts[0] == "GPIO_CONFIG":

            pin = parts[1]
            mode = parts[2]

            if mode != "OUTPUT":
                return "ERROR INVALID_MODE"

            self.gpio_states[pin] = "LOW"

            return f"OK GPIO_CONFIG {pin} OUTPUT"

        if len(parts) == 3 and parts[0] == "GPIO_WRITE":

            pin = parts[1]
            state = parts[2]

            if pin not in self.gpio_states:
                return "ERROR PIN_NOT_CONFIGURED"

            if state not in ["HIGH", "LOW"]:
                return "ERROR INVALID_STATE"

            self.gpio_states[pin] = state

            return f"OK GPIO_WRITE {pin} {state}"

        if len(parts) == 2 and parts[0] == "GPIO_READ":

            pin = parts[1]

            if pin not in self.gpio_states:
                return "ERROR PIN_NOT_CONFIGURED"

            state = self.gpio_states[pin]

            return f"OK GPIO_READ {pin} {state}"

        return "ERROR UNKNOWN_COMMAND"

    # close connection
    def close(self):
        pass