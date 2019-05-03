import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(9, GPIO.OUT)
PWM = GPIO.PWM(10,100)
PWM.start(0)
PWM.ChangeDutyCycle(90)
tones = [184.997, 207.652, 220, 246.942, 277.183, 220, 277.183,277.183, 261.626, 220, 261.626, 
	 261.626, 246.942, 207.652, 246.942, 246.942, 184.997, 207.652, 220, 246.942, 277.183, 
	 369.994, 329.628, 277.183, 220, 277.183, 329.628, 329.628]

try:
	while True:
		for i in tones:
                        PWM.ChangeDutyCycle(90)
			PWM.ChangeFrequency(i)
			time.sleep(0.2)
                        PWM.ChangeDutyCycle(100)
                        time.sleep(0.05)
      
except KeyboardInterrupt:
	pass

PWM.stop()
GPIO.cleanup()
