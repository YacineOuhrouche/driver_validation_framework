# gpio fault injection helper
class GPIOFaultInjector:

    # store device backend
    def __init__(self, device):
        self.device = device

    # send invalid gpio mode
    def invalid_mode(self):
        return self.device.send_command(
            "GPIO_CONFIG PA5 INVALID"
        )

    # send invalid gpio state
    def invalid_state(self):
        return self.device.send_command(
            "GPIO_WRITE PA5 INVALID"
        )

    # send invalid gpio pull
    def invalid_pull(self):
        return self.device.send_command(
            "GPIO_PULL PA5 INVALID"
        )

    # send unknown command
    def unknown_command(self):
        return self.device.send_command(
            "GPIO_WHATEVER PA5"
        )