from Pong import Pong
from SerialHandler import SerialHandler
from Debugger import Debugger

ser = SerialHandler('/dev/ttyAMA0', 9600)
debugger = Debugger()

game = Pong(ser, debugger)
try:
    game.start(10, 5)
except KeyboardInterrupt:
    game.cleanup()
