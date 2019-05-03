from Pong import Pong
from SerialHandler import SerialHandler
from Debugger import Debugger

ser = SerialHandler('/dev/ttyAMA0', 115200)
debugger = Debugger()

game = Pong(ser, debugger)
try:
    game.start(30, 30)
except KeyboardInterrupt:
    game.cleanup()
