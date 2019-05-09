from Pong import Pong
from SerialHandler import SerialHandler
from Debugger import Debugger
import constants
import time

def swapBitsOfByte(n):
    return int('{:08b}'.format(n)[::-1], 2)

ser = SerialHandler('/dev/ttyAMA0', 115200)
debugger = Debugger()

game = Pong(ser, debugger)

for i in range(3, 0, -1):
    game.bus.write_byte(constants.SEVEN_SEG_DISPLAY_ADDR, swapBitsOfByte(i))
    time.sleep(0.4)

game.bus.write_byte(constants.SEVEN_SEG_DISPLAY_ADDR, 0xFF)

try:
    game.start(32, 30)
except KeyboardInterrupt:
    game.cleanup()