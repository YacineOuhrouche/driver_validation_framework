from test_runner.fake_serial import FakeSerial

# verify fake devide respond to ping
def test_fake_serial_ping():
   
    fake = FakeSerial()

    response = fake.send_command("PING")

    assert response == "OK PONG"


# verify invalid command ret an error
def test_fake_serial_unknown_command():

    fake = FakeSerial()

    response = fake.send_command("BAD_COMMAND")

    assert response == "ERROR UNKNOWN_COMMAND"