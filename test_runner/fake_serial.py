from test_runner.device_interface import DeviceInterface


# Mock serial device used for driver validation.
class FakeSerial(DeviceInterface):

    # Initialize simulated GPIO state, mode, pull, and interrupts.
    def __init__(self):
        # gpio states
        self.gpio_states = {}
        self.gpio_modes = {}
        self.gpio_pulls = {}
        self.gpio_interrupts = {}
        self.pending_interrupts = []

        # initialize simulated uart state
        self.uart_config = {}
        self.uart_tx_buffer = []
        self.uart_rx_buffer = []
        self.uart_rx_limit = 3
        self.uart_errors = {}

        # initialize simulated spi state
        self.spi_config = {}
        self.spi_devices = {}

    # Open fake device connection.
    def connect(self):
        pass

    # Process commands and return simulated responses.
    def send_command(self, command: str) -> str:

        parts = command.split()

        if command == "PING":
            return "OK PONG"

        # Configure GPIO mode.
        if len(parts) == 3 and parts[0] == "GPIO_CONFIG":

            pin = parts[1]
            mode = parts[2]

            if mode not in ["OUTPUT", "INPUT"]:
                return "ERROR INVALID_MODE"

            self.gpio_modes[pin] = mode
            self.gpio_pulls[pin] = "NONE"
            self.gpio_states[pin] = "LOW"

            return f"OK GPIO_CONFIG {pin} {mode}"

        # Configure GPIO pull resistor.
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

        # Configure interrupt edge detection.
        if len(parts) == 3 and parts[0] == "GPIO_INTERRUPT":

            pin = parts[1]
            edge = parts[2]

            if pin not in self.gpio_modes:
                return "ERROR PIN_NOT_CONFIGURED"

            if edge not in ["RISING", "FALLING"]:
                return "ERROR INVALID_EDGE"

            self.gpio_interrupts[pin] = edge

            return f"OK GPIO_INTERRUPT {pin} {edge}"

        # Drive GPIO output.
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

        # Simulate external input signal.
        if len(parts) == 3 and parts[0] == "GPIO_SET_INPUT":

            pin = parts[1]
            state = parts[2]

            if pin not in self.gpio_modes:
                return "ERROR PIN_NOT_CONFIGURED"

            if self.gpio_modes[pin] != "INPUT":
                return "ERROR PIN_NOT_INPUT"

            if state not in ["HIGH", "LOW"]:
                return "ERROR INVALID_STATE"

            previous_state = self.gpio_states[pin]

            self.gpio_states[pin] = state

            if pin in self.gpio_interrupts:

                edge = self.gpio_interrupts[pin]

                if (
                    edge == "RISING"
                    and previous_state == "LOW"
                    and state == "HIGH"
                ):
                    self.pending_interrupts.append(pin)

                if (
                    edge == "FALLING"
                    and previous_state == "HIGH"
                    and state == "LOW"
                ):
                    self.pending_interrupts.append(pin)

            return f"OK GPIO_SET_INPUT {pin} {state}"

        # Read GPIO state.
        if len(parts) == 2 and parts[0] == "GPIO_READ":

            pin = parts[1]

            if pin not in self.gpio_modes:
                return "ERROR PIN_NOT_CONFIGURED"

            state = self.gpio_states[pin]

            return f"OK GPIO_READ {pin} {state}"


        # configure uart baud rate
        if len(parts) == 3 and parts[0] == "UART_CONFIG":

            uart = parts[1]
            baud = parts[2]

            if not baud.isdigit():
                return "ERROR INVALID_BAUD"

            self.uart_config[uart] = {
                "baud": int(baud)
            }

            return f"OK UART_CONFIG {uart} {baud}"

        # transmit uart data
        if len(parts) >= 3 and parts[0] == "UART_TX":

            uart = parts[1]
            data = " ".join(parts[2:])

            if uart not in self.uart_config:
                return "ERROR UART_NOT_CONFIGURED"

            self.uart_tx_buffer.append(data)

            return f"OK UART_TX {uart} {data}"

        # inject uart receive data
        if len(parts) >= 3 and parts[0] == "UART_INJECT_RX":

            uart = parts[1]
            data = " ".join(parts[2:])

            if uart not in self.uart_config:
                return "ERROR UART_NOT_CONFIGURED"

            if len(self.uart_rx_buffer) >= self.uart_rx_limit:
                return f"ERROR UART_RX_OVERFLOW {uart}"

            self.uart_rx_buffer.append(data)

            return f"OK UART_INJECT_RX {uart} {data}"

        # read uart received data
        if len(parts) == 2 and parts[0] == "UART_RX":

            uart = parts[1]

            if uart not in self.uart_config:
                return "ERROR UART_NOT_CONFIGURED"

            if not self.uart_rx_buffer:
                return f"OK UART_RX_EMPTY {uart}"

            data = self.uart_rx_buffer.pop(0)

            return f"OK UART_RX {uart} {data}"


        # Check interrupt status.
        if len(parts) == 2 and parts[0] == "GPIO_INTERRUPT_STATUS":

            pin = parts[1]

            if pin in self.pending_interrupts:

                self.pending_interrupts.remove(pin)

                return f"OK GPIO_INTERRUPT {pin}"

            return f"OK GPIO_NO_INTERRUPT {pin}"

         # inject  uart framing error
        if len(parts) == 2 and parts[0] == "UART_INJECT_FRAMING_ERROR":

            uart = parts[1]

            if uart not in self.uart_config:
                return "ERROR UART_NOT_CONFIGURED"

            self.uart_errors[uart] = "FRAMING"

            return f"OK UART_INJECT_FRAMING_ERROR {uart}"

        # read uart error status
        if len(parts) == 2 and parts[0] == "UART_ERROR_STATUS":

            uart = parts[1]

            if uart not in self.uart_config:
                return "ERROR UART_NOT_CONFIGURED"

            error = self.uart_errors.get(uart)

            if not error:
                return f"OK UART_NO_ERROR {uart}"

            self.uart_errors[uart] = None

            return f"OK UART_ERROR {uart} {error}"


                # configure spi mode
        if len(parts) == 5 and parts[0] == "SPI_CONFIG":

            spi = parts[1]
            role = parts[2]
            cpol = parts[3]
            cpha = parts[4]

            if role not in ["MASTER", "SLAVE"]:
                return "ERROR INVALID_SPI_ROLE"

            if cpol not in ["0", "1"]:
                return "ERROR INVALID_CPOL"

            if cpha not in ["0", "1"]:
                return "ERROR INVALID_CPHA"

            self.spi_config[spi] = {
                "role": role,
                "cpol": cpol,
                "cpha": cpha
            }

            return f"OK SPI_CONFIG {spi} {role} CPOL{cpol} CPHA{cpha}"

        # attach simulated spi device
        if len(parts) == 3 and parts[0] == "SPI_ATTACH_DEVICE":

            spi = parts[1]
            device_id = parts[2]

            if spi not in self.spi_config:
                return "ERROR SPI_NOT_CONFIGURED"

            self.spi_devices[device_id] = {
                "spi": spi
            }

            return f"OK SPI_ATTACH_DEVICE {spi} {device_id}"

        # transfer spi data
        if len(parts) >= 4 and parts[0] == "SPI_TRANSFER":

            spi = parts[1]
            device_id = parts[2]
            data = " ".join(parts[3:])

            if spi not in self.spi_config:
                return "ERROR SPI_NOT_CONFIGURED"

            if device_id not in self.spi_devices:
                return "ERROR SPI_DEVICE_NOT_FOUND"

            if self.spi_devices[device_id]["spi"] != spi:
                return "ERROR SPI_DEVICE_BUS_MISMATCH"

            return f"OK SPI_TRANSFER {spi} {device_id} {data}"
            
        return "ERROR UNKNOWN_COMMAND"

    # Close fake device connection.
    def close(self):
        pass