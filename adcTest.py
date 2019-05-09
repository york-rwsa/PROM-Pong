import smbus
import time

i2cAddr = 0x3a

bus = smbus.SMBus(1)
bus.write_byte(i2cAddr, 0xFF)


while True:
    tmp = bus.read_byte(i2cAddr) & 0x7F
    print("{0:b}".format(tmp))
    print(tmp)
    time.sleep(1)
