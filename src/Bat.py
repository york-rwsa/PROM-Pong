import constants
from GameObject import GameObject

class Bat(GameObject):
  def __init__ (self, x, starty, speed, colour, controller, width=1, height=3):
    super().__init__(x, starty, width, height, colour)
    self.speed = speed
    self.controller = controller

  def update(self, timeDiff):
    # controller logic would go here
    # just go up and down in one spot
    controllerPos = self.controller.getPositionPercent() * (24 - self.size.y)

    # if round(controllerPos) == self.pos.y:
    #     return

    if controllerPos > self.pos.y:
        self.pos.y += min(self.speed, controllerPos - self.pos.y)
    elif controllerPos < self.pos.y:
        self.pos.y -= min(self.speed, self.pos.y - controllerPos)

    if self.pos.y + self.size.y >= constants.DISPLAY_HEIGHT:
      self.pos.y = constants.DISPLAY_HEIGHT - self.size.y
    elif self.pos.y <= 0:
      self.pos.y = 0
