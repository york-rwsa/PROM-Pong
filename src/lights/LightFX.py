from PyGlow import PyGlow
from time import sleep

pyglow = PyGlow(speed = 1000) #max brightness 255
pyglow.all(0) #reset LEDs

brightness = 150
speed = 10
speed2 = 5
colors = ["white", "blue", "green", "yellow", "orange", "red"]

def pointWon():
    for c in colors:
        for i in range(0, brightness, speed):
            pyglow.color(c, i)
    for c in colors:
         for i in range(brightness, -1, -speed2):
        pyglow.color(c, i)

'''
RED = [1,7,13]
ORANGE = [2,8,14]
YELLOW = [3,9,15]
GREEN = [4,10,16]
BLUE = [5,11,17]
WHITE = [6,12,18]
'''
