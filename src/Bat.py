import constants
import datetime
from GameObject import GameObject


class Bat(GameObject):
    def __init__(self, x, starty, speed, colour, controller, width=1, height=3):
        super().__init__(x, starty, width, height, colour)
        self.speed = constants.NUMBER_OF_SIZE_INCREASES
        self.controller = controller

        self.sizeIncreasedAt = None
        self.sizeIncreasesLeft = constants.NUMBER_OF_SIZE_INCREASES

    def update(self, timeDiff):
        self.checkSize()
        self.updatePos(self.controller.getPositionPercent() * (24 - self.size.y))

        if self.controller.getTopButton():
            self.increaseSize()

    def updatePos(self, controllerPos):
        if controllerPos > self.pos.y:
            self.pos.y += min(self.speed, controllerPos - self.pos.y)
        elif controllerPos < self.pos.y:
            self.pos.y -= min(self.speed, self.pos.y - controllerPos)

        if self.pos.y + self.size.y >= constants.DISPLAY_HEIGHT:
            self.pos.y = constants.DISPLAY_HEIGHT - self.size.y
        elif self.pos.y <= 0:
            self.pos.y = 0

    def checkSize(self):
        if self.sizeIncreasedAt == None:
            return

        timeDiff = datetime.datetime.now() - self.sizeIncreasedAt

        if timeDiff.total_seconds() > constants.SIZE_INCREASE_TIME:
            self.size.y = int(self.size.y / constants.INCREASE_FACTOR)
            self.sizeIncreasedAt = None

    def increaseSize(self):
        if self.sizeIncreasedAt != None or self.sizeIncreasesLeft == 0:
            return

        self.size.y = int(self.size.y * constants.INCREASE_FACTOR)

        self.sizeIncreasedAt = datetime.datetime.now()
        self.sizeIncreasesLeft -= 1
