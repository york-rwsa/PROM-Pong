import constants

class ControllerHandler:
    def __init__(self, bus, adcAddress):
        self.bus = bus
        self.address = adcAddress

        self.topButton = False
        self.bottomButton = False

        self.lastRawValue = 0

        self.rawValue = 0
        self.scaledValue = 0

        self.lastScaledValue = 0
        self.lastRealValue = 0

        self.alpha = constants.CONTROLLER_ALPHA

    def getPositionPercent(self):
        self.readAdc()

        self.rawValue = self.alpha * self.lastRawValue + (1 - self.alpha) * self.lastRawValue
        self.scaledValue = self.alpha * self.lastScaledValue + (1 - self.alpha) * self.lastScaledValue

        return self.scaledValue

    def readAdc(self):
        raise NotImplementedError

    def getTopButton(self):
        tmp = self.topButton
        self.topButton = False

        return tmp

    def getBottomButton(self):
        tmp = self.bottomButton
        self.bottomButton = False

        return tmp

class OnBoardADCHandler(ControllerHandler):
    def __init__(self, bus, adcAddress, adcCmdCode):
        super().__init__(bus, adcAddress)
        self.adcCmdCode = adcCmdCode

    def readAdc(self):
        self.bus.write_byte(self.address, self.adcCmdCode)
        tmp = self.bus.read_word_data(self.address, 0x00)

        rawValue = ((tmp & 0x0F) << 8) | ((tmp & 0xFF00) >> 8)
        scaledValue = (rawValue / 4092.0)

        self.lastRawValue = rawValue
        self.lastScaledValue = scaledValue

        return scaledValue

class CPLDHandler(ControllerHandler):
    def __init__(self, bus, adcAddress):
        super().__init__(bus, adcAddress)

        self.bus.write_byte(self.address, 0xFF)

    def readAdc(self):
        # this is a 7 bit adc, hence masking msb
        tmp = self.bus.read_byte(self.address) & 0x7F
        scaledValue = tmp / constants.CPLD_MAX_RANGE

        self.lastRawValue = tmp
        self.lastScaledValue = scaledValue
        self.lastRealValue = scaledValue * constants.CPLD_VOLTAGE_AT_MAX

        return scaledValue
