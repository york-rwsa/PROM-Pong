import TerminalHandler
import time
import GameObject

handler = TerminalHandler.TerminalHandler()
obj = GameObject.GameObject()
obj.size.setxy(3, 6)

handler.writeState(obj.render())

time.sleep(2)

obj.colour = "red"
obj.pos.setcoors(4, 6)

handler.writeState(obj.render())

while(True):
  pass