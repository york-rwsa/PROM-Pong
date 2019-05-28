import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

high = GPIO.PWM(9,100)
high.start(0)
high.ChangeDutyCycle(85)

bass = GPIO.PWM(11,100)
bass.start(0)
bass.ChangeDutyCycle(50)

highTones = [184.997, 207.652, 220, 246.942, 277.183, 220, 277.183,277.183, 261.626, 220, 261.626,
             261.626, 246.942, 207.652, 246.942, 246.942, 184.997, 207.652, 220, 246.942, 277.183,
             220, 277.183, 390.994, 340.628, 277.183, 220, 277.183, 340.628, 340.628, 340.628, 340.628]

bassTones = [92.499, 92.499, 138.591, 138.591, 92.499, 92.499, 138.591, 138.591, 146.832, 146.832,
             73.416, 73.416, 69.296, 69.296, 138.591, 138.591, 92.499, 92.499, 138.591, 138.591,
             92.499, 92.499, 138.591, 138.591, 55, 55, 110, 110, 55, 55, 110, 110]

try:
    while True:
        for i, highTone in enumerate(highTones):
            high.ChangeFrequency(highTone * 2)
            high.ChangeDutyCycle(85)

            bass.ChangeFrequency(bassTones[i]) 
            bass.ChangeDutyCycle(50)

            time.sleep(0.2)
            high.ChangeDutyCycle(100)
            high.ChangeDutyCycle(100)
            time.sleep(0.05)

except KeyboardInterrupt:
    pass

PWM.stop()
GPIO.cleanup()
