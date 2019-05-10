import RPi.GPIO as GPIO
import time
import multiprocessing

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

        self.process = None

    def playTone(self, seconds, freq=100, dc=50):
        self.pwm.ChangeFrequency(freq)
        self.pwm.start(dc)

        time.sleep(seconds)

        self.pwm.stop()

    def playMusic(self, onDutyCycle):
        self.pwm.start(0)

        while True:
            for i, tone in enumerate(self.highTones):
                self.pwm.ChangeFrequency(tone * 2)
                self.pwm.ChangeDutyCycle(onDutyCycle)
                time.sleep(0.2)
                self.pwm.ChangeDutyCycle(100)

    def asyncPlayTone(self, seconds, freq=100, dc=50):
        if self.process is None or not self.process.is_alive():
            self.process = multiprocessing.Process(target=self.playTone, args=(seconds, freq, dc))
            self.process.start()

    def asyncPlayMusic(self, onDutyCycle=50):
        if self.process is None or not self.process.is_alive():
            self.process = multiprocessing.Process(target=self.playMusic, args=(onDutyCycle,))
            self.process.start()

    def killProcess(self):
        if self.process is not None and self.process.is_alive():
            self.process.terminate()

    def stopOutput(self):
        self.killProcess()
        self.pwm.stop()

    def cleanup(self):
        self.stopOutput()
        GPIO.cleanup()
