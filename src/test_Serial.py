from Pong import Pong
from SerialHandler import SerialHandler

ser = SerialHandler('/dev/ttyAMA0', 9600)

game = Pong(ser)
game.start(10, 5)
