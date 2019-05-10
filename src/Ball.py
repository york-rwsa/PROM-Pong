import constants
import random
from Vector import Vector
from GameObject import GameObject
from sound import sound

class Ball(GameObject):
    def __init__(self, x, starty, speed, colour, collidableObjects=[], angle=45, width=3, height=2):
        super().__init__(x, starty, width, height, colour)
        self.speed = speed
        self.velocity = Vector.createUnitVectorFromAngle(angle)
        self.collidableObjects = collidableObjects
        self.collision = False
        self.serving = None
        self.sfx = sound.Sound(constants.MUSIC_SFX_PIN)

    def update(self, timeDiff):
        if self.serving != None:
            return

        self.collision = self.handleCollisions(timeDiff)

        if self.collision:
            self.sfx.asyncPlayTone(constants.MUSIC_SFX_DELAY, constants.MUSIC_SFX_FREQ)

        self.pos += self.velocity * self.speed * timeDiff

    def handleCollisions(self, timeDiff):
        collisionThisUpdate = False

        for obj in self.collidableObjects:
            if self.detectColisionX(obj, timeDiff):
                if not self.collision:
                    self.velocity.x *= -1
                collisionThisUpdate = True


            if self.detectColisionY(obj, timeDiff):
                if not self.collision:
                    self.velocity.y *= -1
                collisionThisUpdate = True

        return collisionThisUpdate

    def nextPos(self, timeDiff):
        return self.pos + self.velocity * self.speed * timeDiff

    def detectColisionX(self, obj, timeDiff):
        nextPos = self.nextPos(timeDiff)

        return (
            nextPos.x + self.size.x > obj.pos.x and
            nextPos.x < obj.pos.x + obj.size.x and
            self.pos.y + self.size.y > obj.pos.y and
            self.pos.y < obj.pos.y + obj.size.y
        )

    def detectColisionY(self, obj, timeDiff):
        nextPos = self.nextPos(timeDiff)

        return (
            nextPos.y + self.size.y > obj.pos.y and
            nextPos.y < obj.pos.y + obj.size.y and
            self.pos.x + self.size.x > obj.pos.x and
            self.pos.x < obj.pos.x + obj.size.x
        )
