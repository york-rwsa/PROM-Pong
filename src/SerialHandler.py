from serial import Serial
import time

class SerialHandler:
    def __init__(self, port, baudRate):
        self.serialPort = Serial(port, baudRate)

    def write(self, data):
        if self.serialPort.isOpen() == False:
            self.serialPort.open()

        print(repr(data))
        self.serialPort.write(bytes(data, 'utf-8'))

    def close(self):
        self.serialPort.close()

    def flush(self):
        pass
