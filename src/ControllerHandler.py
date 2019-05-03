class ControllerHandler:
    def __init__(self, bus, adcAddress, adcCmdCode):
        self.bus = bus
        self.address = adcAddress
        self.adcCmdCode = adcCmdCode

        self.topButton = False
        self.bottomButton = False

        self.lastRawValue = 0
        self.lastScaledValue = 0

    def getPositionPercent(self):
        return self.readAdc()

    def readAdc(self):
        self.bus.write_byte(self.address, self.adcCmdCode)
        tmp = self.bus.read_word_data(self.address, 0x00)

        rawValue = ((tmp & 0x0F) << 8) | ((tmp & 0xFF00) >> 8)
        scaledValue = (rawValue / 4092.0)

        self.lastRawValue = rawValue
        self.lastScaledValue = scaledValue

        return scaledValue

    def getTopButton(self):
        tmp = self.topButton
        self.topButton = False

        return tmp

    def getBottomButton(self):
        tmp = self.bottomButton
        self.bottomButton = False

        return tmp
