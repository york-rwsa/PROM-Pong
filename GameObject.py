from Vector import Vector
import constants

class GameObject:
  def __init__ (self):
    self.pos = Vector(0, 0)
    self.size = Vector(0, 0)
    self.velocity = Vector(0, 0)
    self.colour = "white"
  
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