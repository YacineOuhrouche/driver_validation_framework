from test_runner.device_interface import DeviceInterface

# Mock serial device used for testing
class FakeSerial(DeviceInterface):
    
    # open a fake conn
    def connect(self):
        pass

    # return simulated respinse
    def send_command(self, command: str) -> str:

        responses = {
            "PING": "OK PONG",
            "GPIO_CONFIG PA5 OUTPUT": "OK GPIO_CONFIG PA5 OUTPUT",
            "GPIO_WRITE PA5 HIGH": "OK GPIO_WRITE PA5 HIGH",
            "GPIO_WRITE PA5 LOW": "OK GPIO_WRITE PA5 LOW",
            "GPIO_READ PA5": "OK GPIO_READ PA5 LOW",
        }

        
        return responses.get(command,"ERROR UNKNOWN_COMMAND" )

    # close fake connection
    def close(self):
        pass