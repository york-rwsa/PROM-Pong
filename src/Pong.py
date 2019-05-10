from Word import Word
from Game import Game
from GameObject import GameObject
from Number import Number
from Ball import Ball
from Bat import Bat
from Vector import Vector
from itertools import cycle
from ControllerHandler import OnBoardADCHandler, CPLDHandler
import random
import constants
import smbus
import lights.LightFX as pointGlow
import RPi.GPIO as GPIO
from sys import stdout

class Pong(Game):
    def __init__(self, terminalHandler=stdout, debug=None):
        super().__init__(terminalHandler, debug)

        self.bus = smbus.SMBus(1)
        self.bus.write_byte(constants.BAT_BUTTONS_I2C_ADDRESS, 0xFF)
        self.bus.write_byte(constants.BALL_LED_I2C_ADDRESS, 0xFF)

        self.batButtonState = 0xFF

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(constants.BAT_BUTTONS_INTERRUPT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(
            constants.BAT_BUTTONS_INTERRUPT_PIN, GPIO.FALLING, callback=self.handleControllerInterrupt)

        for pin in constants.LED_PINS:
            GPIO.setup(pin, GPIO.OUT)
        self.lastLED = None

        self.scoreLeft = Number(0, 29, 2, "cyan")
        self.scoreRight = Number(0, 49, 2, "pink")

        self.leftController = CPLDHandler(
            self.bus, constants.LEFT_BAT_I2C_ADDRESS
        )
        self.rightController = OnBoardADCHandler(self.bus, constants.RIGHT_BAT_I2C_ADDRESS, constants.RIGHT_BAT_CMD_CODE)

        self.batLeft = Bat(3, 12, 6, "cyan", self.leftController)
        self.batRight = Bat(77, 12, -6, "pink", self.rightController)

        self.edges = [
            GameObject(0, -1, constants.PONG_WIDTH, 1, "red"),
            #deleted the "+1" that followed constants.PONG_HEIGHT
            GameObject(0, constants.PONG_HEIGHT + 1,
                       constants.PONG_WIDTH, 1, "red"),
        ]

        self.ball = Ball(
            10, 20, constants.SERVE_SPEED, "green", self.edges +
            [self.batLeft, self.batRight], 25, 1, 1
        )

        self.addObjects(
            [self.scoreLeft, self.scoreRight, self.batLeft, self.batRight, self.ball]
            + self.edges
        )

        self.ball.serving = 'right'
        self.serves = 0

        self.gameOver = False
        self.winnerText = None

    def score(self, scorer):
        pointGlow.asyncStart()
        if scorer == 'left':
            self.scoreLeft.value += 1
        elif scorer == 'right':
            self.scoreRight.value += 1

        self.ball.serving = 'left' if (self.serves // 5 % 2) else 'right'
        self.leftController.getBottomButton()
        self.rightController.getBottomButton()

        if self.scoreLeft.value >= constants.WIN_POINT_COUNT:
            self.gameOver = True
            self.winnerText = Word("PLAYER 1 WINS!", 12, 10, "red")
        elif self.scoreRight.value >= constants.WIN_POINT_COUNT:
            self.gameOver = True
            self.winnerText = Word("PLAYER 2 WINS!", 12, 10, "red")

        self.ball.speed = constants.SERVE_SPEED

    def serve(self):
        if self.ball.serving == 'left':
            self.ball.velocity = Vector.createUnitVector(1, 1)
        elif self.ball.serving == 'right':
            self.ball.velocity = Vector.createUnitVector(-1, 1)

        self.ball.serving = None
        self.serves += 1

    def update(self, delta):
        if (self.gameOver):
            return

        super().update(delta)

        if self.ball.pos.x < 0:
            # ball dead player two gains point
            self.score('right')
        elif self.ball.pos.x + self.ball.size.x > constants.PONG_WIDTH:
            # ball dead player two gains point
            self.score('left')

        # check ball is still in region
        # abs means absolute (+ve) value, ie abs(-19) == abs(19) == 19
        if self.ball.pos.y < 0:
            self.ball.pos.y = 0
            self.ball.velocity.y = abs(self.ball.velocity.y)
        elif self.ball.pos.y > 24:
            self.ball.pos.y = 24
            self.ball.velocity.y = -abs(self.ball.velocity.y)

        # serve logic
        if self.ball.serving != None:
            if self.ball.serving == 'left':
                self.ball.pos.x = self.batLeft.pos.x + 1
                self.ball.pos.y = self.batLeft.pos.y + int((self.batLeft.size.y - 1) / 2)

                if self.batLeft.controller.getBottomButton():
                    self.serve()


            elif self.ball.serving == 'right':
                self.ball.pos.x = self.batRight.pos.x - 1
                self.ball.pos.y = self.batRight.pos.y + int((self.batRight.size.y - 1) / 2)

                if self.batRight.controller.getBottomButton():
                    self.serve()

        self.writeBallPosToLEDS()

    def writeBallPosToLEDS(self):
        led = int(max(0, round(self.ball.pos.x / 10) - 1))

        if self.lastLED != led:
            if self.lastLED is not None:
                GPIO.output(constants.LED_PINS[self.lastLED], GPIO.LOW)
            GPIO.output(constants.LED_PINS[led], GPIO.HIGH)

            self.bus.write_byte(constants.BALL_LED_I2C_ADDRESS, 0xFF & ~(1 << led))

        self.lastLED = led

    def render(self, delta):
        if self.gameOver:
            self.output.writeState(self.winnerText.render())
            return

        state = {}
        # render net
        state.update(
            {
                (40, y): "yellow"
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
        self.batButtonState = input

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

    def debug(self, delta, output=[]):
        output = [
            ('Pong', [
                "Left Controller: {} (raw), ~{:.2f}V".format(
                    self.leftController.rawValue,
                    self.leftController.lastScaledValue * constants.CPLD_VOLTAGE_AT_MAX
                ),
                "Right Controller: {} (raw), ~{:.2f}V".format(
                    self.rightController.rawValue,
                    self.rightController.lastScaledValue * 3.2
                )
            ]),
            ('Ball', [
                "Position: x: {:.2f}, y: {:.2f}".format(self.ball.pos.x, self.ball.pos.y),
                "Angle: {:.2f} degrees".format(self.ball.velocity.arg()),
                "Trajectory: x: {:.2f}, y: {:.2f}".format(self.ball.velocity.x, self.ball.velocity.y),
                "Speed: {}".format(self.ball.speed)
            ]),
            ('Left Bat', [
                "Position: y: {:.2f}".format(self.batLeft.pos.y),
                "Size increases left: {}".format(self.batLeft.sizeIncreasesLeft),
                "Top button: {}, Bottom button: {}".format(self.batButtonState & constants.LEFT_BAT_TOP_BUTTON == 0,
                                                           self.batButtonState & constants.LEFT_BAT_BOT_BUTTON == 0),
                "Handler: {}".format(self.leftController.__class__.__name__)
            ]),
            ('Right Bat', [
                "Position: y: {:.2f}".format(self.batRight.pos.y),
                "Size increases left: {}".format(self.batRight.sizeIncreasesLeft),
                "Top button: {}, Bottom button: {}".format(self.batButtonState & constants.RIGHT_BAT_TOP_BUTTON == 0,
                                                           self.batButtonState & constants.RIGHT_BAT_BOT_BUTTON == 0),
                "Handler: {}".format(self.rightController.__class__.__name__)
            ])
        ]

        super().debug(delta, output)
