import pytest
from test_runner.serial_client import SerialClient


def test_serial_client_requires_port(monkeypatch):
    monkeypatch.delenv("SERIAL_PORT", raising=False)

    client = SerialClient()

    with pytest.raises(ValueError):
        client.connect()