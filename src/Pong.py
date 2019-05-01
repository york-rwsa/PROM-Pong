from Game import Game
from GameObject import GameObject
from Number import Number
from Ball import Ball
from Bat import Bat
from Vector import Vector
from itertools import cycle
from ControllerHandler import ControllerHandler
import random
import constants
import smbus
import RPi.GPIO as GPIO


class Pong(Game):
    def __init__(self, debug=False):
        super().__init__(debug)

        self.bus = smbus.SMBus(1)
        self.bus.write_byte(constants.BAT_BUTTONS_I2C_ADDRESS, 0xFF)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(
            10, GPIO.FALLING, callback=self.handleControllerInterrupt)

        self.scoreLeft = Number(0, 29, 1, "red")
        self.scoreRight = Number(0, 49, 1, "blue")

        self.leftController = ControllerHandler(
            self.bus, constants.LEFT_BAT_I2C_ADDRESS, constants.LEFT_BAT_CMD_CODE
        )
        self.rightController = ControllerHandler(
            self.bus, constants.RIGHT_BAT_I2C_ADDRESS, constants.RIGHT_BAT_CMD_CODE
        )

        self.batLeft = Bat(3, 12, 6, "red", self.leftController)
        self.batRight = Bat(77, 12, -6, "blue", self.rightController)

        self.edges = [
            GameObject(0, -1, constants.PONG_WIDTH, 1, "reset"),
            GameObject(0, constants.PONG_HEIGHT + 1,
                       constants.PONG_WIDTH, 1, "reset"),
        ]

        self.ball = Ball(
            10, 20, 10, "red", self.edges +
            [self.batLeft, self.batRight], 25, 1, 1
        )

        self.addObjects(
            [self.scoreLeft, self.scoreRight, self.batLeft, self.batRight, self.ball]
            + self.edges
        )

        self.resetBall()

    def resetBall(self):
        self.ball.pos.setxy(40, 12)
        self.ball.velocity = Vector.createUnitVector(random.randint(0, 360))

    def update(self, delta):
        if self.ball.pos.x < 0:
            # ball dead player two gains point
            self.scoreRight.value += 1
            self.resetBall()
        elif self.ball.pos.x + self.ball.size.x > constants.PONG_WIDTH:
            # ball dead player two gains point
            self.scoreLeft.value += 1
            self.resetBall()

        super().update(delta)

    def render(self, delta):
        state = {}
        # render net
        state.update(
            {
                (40, y): "blue"
                for (y, draw) in zip(
                    range(constants.PONG_HEIGHT), cycle(
                        [False, False, True, True])
                )
                if draw
            }
        )

        super().render(delta, state)

    def handleControllerInterrupt(self, channel):
        input = self.bus.read_byte(constants.BAT_BUTTONS_I2C_ADDRESS)

        if input == 255:
            return

        if input & constants.RIGHT_BAT_TOP_BUTTON == 0:
            self.rightController.topButton = True
        if input & constants.RIGHT_BAT_BOT_BUTTON == 0:
            self.rightController.bottomButton = True

        if input & constants.LEFT_BAT_TOP_BUTTON == 0:
            self.leftController.topButton = True
        if input & constants.LEFT_BAT_BOT_BUTTON == 0:
            self.leftController.bottomButton = True
