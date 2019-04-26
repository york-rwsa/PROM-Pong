import smbus
import time

i2cAddr = 0x21
code = 0x10

bus = smbus.SMBus(1)
bus.write_byte(i2cAddr, code)
tmp = bus.read_word_data(i2cAddr, 0x00)
print("{0:b}".format(tmp))
print(tmp)
