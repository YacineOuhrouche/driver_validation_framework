#mock serial device used for testing eithout stm32 hw
class FakeSerial:
    def __init__(self):
        self.last_command = ""

    # store last command sent by the test
    def write(self, data: bytes):
        self.last_command = data.decode().strip()

    # return a simulated device response
    def readline(self) -> bytes:
        responses = {
            "PING": "OK PONG",
            "GPIO_CONFIG PA5 OUTPUT": "OK GPIO_CONFIG PA5 OUTPUT",
            "GPIO_WRITE PA5 HIGH": "OK GPIO_WRITE PA5 HIGH",
            "GPIO_WRITE PA5 LOW": "OK GPIO_WRITE PA5 LOW",
            "GPIO_READ PA5": "OK GPIO_READ PA5 LOW",
        }

        response = responses.get(self.last_command, "ERROR UNKNOWN_COMMAND")
        return f"{response}\n".encode()

    # close mock connection
    def close(self):
        pass