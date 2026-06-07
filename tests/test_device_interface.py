from test_runner.fake_serial import FakeSerial


# verify ping
def test_ping():

    device = FakeSerial()

    device.connect()

    response = device.send_command("PING")

    assert response == "OK PONG"

    device.close()


# verify invalif command handling
def test_invalid_command():


    device = FakeSerial()

    device.connect()

    response = device.send_command("BAD_COMMAND")

    assert response == "ERROR UNKNOWN_COMMAND"

    device.close()