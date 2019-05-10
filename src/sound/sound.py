import RPi.GPIO as GPIO
import time
from threading import Thread



class Sound:
    highTones = [184.997, 207.652, 220, 246.942, 277.183, 220, 277.183,277.183, 261.626, 220, 261.626,
                 261.626, 246.942, 207.652, 246.942, 246.942, 184.997, 207.652, 220, 246.942, 277.183,
                 220, 277.183, 390.994, 340.628, 277.183, 220, 277.183, 340.628, 340.628, 340.628, 340.628]

    def __init__(self, outputPin):
        self.pin = outputPin

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.pin, 100)

        self.thread = None

    def playTone(self, seconds, freq=100, dc=50):
        self.pwm.ChangeFrequency(freq)
        self.pwm.start(dc)

        time.sleep(seconds)

        self.pwm.stop()

    def playMusic(self):
        self.pwm.start(0)

        while True:
            for i, tone in enumerate(self.highTones):
                self.pwm.ChangeFrequency(tone * 2)
                self.pwm.ChangeDutyCycle(85)
                time.sleep(0.2)
                self.pwm.ChangeDutyCycle(100)

    def asyncPlayTone(self, seconds, freq=100, dc=50):
        if self.thread is None:
            self.thread = Thread(target=self.playTone, args=(seconds, freq, dc))
            self.thread.start()

    def asyncPlayMusic(self):
        if self.thread is None:
            self.thread = Thread(target=self.playMusic)
            self.thread.start()

    def cleanup():
        self.pwm.stop()
        GPIO.cleanup()
