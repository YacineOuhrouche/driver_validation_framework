from test_runner.fake_serial import FakeSerial

# verify fake device response to ping
def test_fake_serial_ping():
    fake = FakeSerial()

    fake.write(b"PING\n")
    response = fake.readline().decode().strip()

    assert response == "OK PONG"


# verigy that invalid command ret an error 
def test_fake_serial_unknown_command():
    fake = FakeSerial()

    fake.write(b"BAD_COMMAND\n")
    response = fake.readline().decode().strip()

    assert response == "ERROR UNKNOWN_COMMAND"