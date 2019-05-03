from PyGlow import PyGlow
from time import sleep
pyglow = PyGlow(speed = 1000) #max brightness 255
pyglow.all(0) #reset LEDs
brightness = 150
speed = 10
speed2 = 5

def pointWon():
    for i in range(0, brightness, speed):
        pyglow.color("white", i)
    for i in range(0, brightness, speed):
        pyglow.color("blue", i)
    for i in range(0, brightness, speed):
            pyglow.color("green", i)
    for i in range(0, brightness, speed):
        pyglow.color("yellow", i)
    for i in range(0, brightness, speed):
        pyglow.color("orange", i)
    for i in range(0, brightness, speed):
        pyglow.color("red", i)
    sleep(.2)
    for i in range(brightness, -1, -speed2):
        pyglow.color("white", i)
    for i in range(brightness, -1, -speed2):
        pyglow.color("blue", i)
    for i in range(brightness, -1, -speed2):
            pyglow.color("green", i)
    for i in range(brightness, -1, -speed2):
        pyglow.color("yellow", i)
    for i in range(brightness, -1, -speed2):
        pyglow.color("orange", i)
    for i in range(brightness, -1, -speed2):
        pyglow.color("red", i)





'''
RED = [1,7,13]
ORANGE = [2,8,14]
YELLOW = [3,9,15]
GREEN = [4,10,16]
BLUE = [5,11,17]
WHITE = [6,12,18]
'''
