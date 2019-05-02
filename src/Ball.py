import constants
from Vector import Vector
from GameObject import GameObject


class Ball(GameObject):
    def __init__(self, x, starty, speed, colour, collidableObjects=[], angle=45, width=3, height=2):
        super().__init__(x, starty, width, height, colour)
        self.speed = speed
        self.velocity = Vector.createUnitVector(angle)
        self.collidableObjects = collidableObjects
        self.collision = False
        self.serving = None

    def update(self, timeDiff):
        if self.serving != None:
            return

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

        self.collision = collisionThisUpdate

        self.pos += self.velocity * self.speed * timeDiff

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
