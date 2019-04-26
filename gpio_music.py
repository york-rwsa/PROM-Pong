import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.OUT)
PWM = GPIO.PWM(10,100)
PWM.start(0)
PWM.ChangeDutyCycle(90)
tones = [195.998, 195.998, 391.995, 195.998, 195.998, 391.995, 195.998, 195.998, 233.082, 466.164, 932.328, 233.082, 466.164, 932.328, 233.082, 466.164, 261.626, 523.251, 1046.502, 261.626, 523.251, 1046.502, 261.626, 523.251, 1244.508, 622.254, 311.127, 1244.508, 622.254, 311.127, 1244.508, 622.254]

try:
	while True:
		for i in tones:
                        PWM.ChangeDutyCycle(90)
			PWM.ChangeFrequency(2*i)
			time.sleep(0.2)
                        PWM.ChangeDutyCycle(100)
                        time.sleep(0.05)
      
except KeyboardInterrupt:
	pass

PWM.stop()
GPIO.cleanup()
