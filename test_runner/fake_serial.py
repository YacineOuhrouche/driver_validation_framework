from test_runner.device_interface import DeviceInterface


# mock serial device 
class FakeSerial(DeviceInterface):

    # initialize simulated GPIO state and mode
    def __init__(self):
        self.gpio_states = {}
        self.gpio_modes = {}

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

            if mode not in ["OUTPUT", "INPUT"]:
                return "ERROR INVALID_MODE"

            self.gpio_modes[pin] = mode
            self.gpio_states[pin] = "LOW"

            return f"OK GPIO_CONFIG {pin} {mode}"

        if len(parts) == 3 and parts[0] == "GPIO_WRITE":

            pin = parts[1]
            state = parts[2]

            if pin not in self.gpio_modes:
                return "ERROR PIN_NOT_CONFIGURED"

            if self.gpio_modes[pin] != "OUTPUT":
                return "ERROR PIN_NOT_OUTPUT"

            if state not in ["HIGH", "LOW"]:
                return "ERROR INVALID_STATE"

            self.gpio_states[pin] = state

            return f"OK GPIO_WRITE {pin} {state}"

        if len(parts) == 3 and parts[0] == "GPIO_SET_INPUT":

            pin = parts[1]
            state = parts[2]

            if pin not in self.gpio_modes:
                return "ERROR PIN_NOT_CONFIGURED"

            if self.gpio_modes[pin] != "INPUT":
                return "ERROR PIN_NOT_INPUT"

            if state not in ["HIGH", "LOW"]:
                return "ERROR INVALID_STATE"

            self.gpio_states[pin] = state

            return f"OK GPIO_SET_INPUT {pin} {state}"

        if len(parts) == 2 and parts[0] == "GPIO_READ":

            pin = parts[1]

            if pin not in self.gpio_modes:
                return "ERROR PIN_NOT_CONFIGURED"

            state = self.gpio_states[pin]

            return f"OK GPIO_READ {pin} {state}"

        return "ERROR UNKNOWN_COMMAND"

    # close fake device connection
    def close(self):
        pass