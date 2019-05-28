import time
import RPi.GPIO as gpio
import smbus

address = 0x38
bus = smbus.SMBus(1)
bus.write_byte(address, 0xFF)

gpio.setmode(gpio.BCM)
gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_UP)

def callback(channel):
  print(str(bus.read_byte(address)))

gpio.add_event_detect(10, gpio.FALLING, callback=callback, bouncetime=300)

try:
  while True:
    print('waiting')
    time.sleep(1)
except:
  gpio.cleanup()

