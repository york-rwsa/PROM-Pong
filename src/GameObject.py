from Vector import Vector
import constants

class GameObject:
  def __init__ (self, x=0, y=0, width=1, height=1, colour="white"):
    self.pos = Vector(x, y)
    self.size = Vector(width, height)
    self.velocity = Vector(0, 0)
    self.colour = colour
  
  def render (self):
    # self.pos defined as the top left corner
    startx = int(round(self.pos.x))
    starty = int(round(self.pos.y))

    return {
      (x, y): self.colour
      for x in range(startx, startx + self.size.x)
      for y in range(starty, starty + self.size.y)
      if x >= 0 and x < constants.DISPLAY_WIDTH and
         y >= 0 and y < constants.DISPLAY_HEIGHT
    }
  
  def update (self, timeDiff):
    self.pos += self.velocity * timeDiff