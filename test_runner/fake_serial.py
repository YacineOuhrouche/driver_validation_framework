from test_runner.device_interface import DeviceInterface


# Mock serial device used for driver validation
class FakeSerial(DeviceInterface):

    # Initialize simulated GPIO state, mode, and pull
    def __init__(self):
        self.gpio_states = {}
        self.gpio_modes = {}
        self.gpio_pulls = {}

    # Open fake device connection
    def connect(self):
        pass

    # Process commands and return simulated responses
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
            self.gpio_pulls[pin] = "NONE"
            self.gpio_states[pin] = "LOW"

            return f"OK GPIO_CONFIG {pin} {mode}"

        if len(parts) == 3 and parts[0] == "GPIO_PULL":

            pin = parts[1]
            pull = parts[2]

            if pin not in self.gpio_modes:
                return "ERROR PIN_NOT_CONFIGURED"

            if self.gpio_modes[pin] != "INPUT":
                return "ERROR PIN_NOT_INPUT"

            if pull not in ["UP", "DOWN", "NONE"]:
                return "ERROR INVALID_PULL"

            self.gpio_pulls[pin] = pull

            if pull == "UP":
                self.gpio_states[pin] = "HIGH"

            if pull == "DOWN":
                self.gpio_states[pin] = "LOW"

            return f"OK GPIO_PULL {pin} {pull}"

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

    # Close fake device connection
    def close(self):
        pass