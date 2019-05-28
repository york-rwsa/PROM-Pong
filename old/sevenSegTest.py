import smbus
import time

def swapBitsOfByte(n):
    return int('{:08b}'.format(n)[::-1], 2)

addr = 0x23
bus = smbus.SMBus(1)

for i in range(10):
    tmp = swapBitsOfByte(i)
    bus.write_byte(addr, tmp)
    print(i)
    print("{0:b}".format(tmp))
    time.sleep(2)

