import os
import serial
from dotenv import load_dotenv


load_dotenv()


class SerialClient:
    def __init__(self):
        self.port = os.getenv("SERIAL_PORT")
        self.baud_rate = int(os.getenv("BAUD_RATE", "115200"))
        self.timeout = float(os.getenv("TIMEOUT", "2"))
        self.connection = None

    def connect(self):
        if not self.port:
            raise ValueError("SERIAL_PORT is missing in .env")

        self.connection = serial.Serial(
            port=self.port,
            baudrate=self.baud_rate,
            timeout=self.timeout,
        )

    def send_command(self, command: str) -> str:
        if self.connection is None:
            raise RuntimeError("Serial connection is not open")

        full_command = command.strip() + "\n"
        self.connection.write(full_command.encode())

        response = self.connection.readline().decode().strip()
        return response

    def close(self):
        if self.connection:
            self.connection.close()