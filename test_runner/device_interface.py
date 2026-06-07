
#Common interface for all device communication backends.


#Defines the required communication methods

class DeviceInterface:
    
    # open connection to dev
    def connect(self):
        raise NotImplementedError

    # send command and ret response
    def send_command(self, command: str) -> str:

        raise NotImplementedError

    # close connectioj
    def close(self):
        raise NotImplementedError