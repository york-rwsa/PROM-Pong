import constants
from GameObject import GameObject

class Bat(GameObject):
  def __init__ (self, x, starty, speed, colour, width=1, height=3):
    super().__init__(x, starty, width, height, colour)
    self.speed = speed

  def update(self, timeDiff):
    # controller logic would go here
    # just go up and down in one spot
    self.pos.y += timeDiff * self.speed 

    if self.pos.y + self.size.y >= constants.DISPLAY_HEIGHT or self.pos.y <= 0 + constants.DISPLAY_OFFSET:
      self.speed *= -1
      