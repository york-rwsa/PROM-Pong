from PyGlow import PyGlow
from time import sleep
pyglow = PyGlow(speed = 1000) #max brightness 255
pyglow.all(0) #reset LEDs


def LEDFx(): #flash in LEDs 3 at a time (colors). Gradually fade out each
    pyglow.color("red", 150)

    pyglow.color("orange", 150)
    pyglow.color("red", 100)

    pyglow.color("yellow", 150)
    pyglow.color("red", 50)
    pyglow.color("orange", 100)
    

    pyglow.color("green", 150)
    pyglow.color("red", 10)
    pyglow.color("orange", 50)
    pyglow.color("yellow", 100)
    

    pyglow.color("blue", 150)
    pyglow.color("red", 0)
    pyglow.color("orange", 10)
    pyglow.color("yellow", 50)
    pyglow.color("green", 100)
    

    pyglow.color("white", 150)
    pyglow.color("orange", 0)
    pyglow.color("yellow", 10)
    pyglow.color("green", 50)

    pyglow.color("yellow", 0)
    pyglow.color("green", 10)
    pyglow.color("white", 100)

    pyglow.color("green", 0)
    pyglow.color("white", 50)

    pyglow.color("white", 10)
    pyglow.color("white", 0)
    

    #turn on all LEDs and turn off three at a time
    sleep(0.5)
    pyglow.all(150)
    
    pyglow.color("red", 0)
    pyglow.color("yellow", 0)
    pyglow.color("blue", 0)

    sleep(0.1)
    
    pyglow.color("orange", 0)
    pyglow.color("green", 0)
    pyglow.color("white", 0)
    


    

while(True):
  LEDFx()




        
'''
RED = [1,7,13]
ORANGE = [2,8,14]
YELLOW = [3,9,15]
GREEN = [4,10,16]
BLUE = [5,11,17]
WHITE = [6,12,18]



def LEDFx1(): #flash in LEDs 3 at a time. Gradually fade out each triple
    while True:
        pyglow.set_leds(RED, 150) #set red leds
        
        pyglow.update_leds()
        sleep(0.05)
        
        pyglow.set_leds(RED, 50) #turn down red leds
        pyglow.set_leds(ORANGE, 150) #set orange leds

        pyglow.update_leds()
        sleep(0.05)

        pyglow.set_leds(RED, 25) #turn down red leds
        pyglow.set_leds(ORANGE, 50)
        pyglow.set_leds(YELLOW, 150)

        pyglow.update_leds()
        sleep(0.05)

        pyglow.set_leds(RED, 0)
        pyglow.set_leds(ORANGE, 25)
        pyglow.set_leds(YELLOW, 50)
        pyglow.set_leds(GREEN, 150)
        
        pyglow.update_leds()
        sleep(0.05)

        pyglow.set_leds(ORANGE, 0)
        pyglow.set_leds(YELLOW, 25)
        pyglow.set_leds(GREEN, 50)
        pyglow.set_leds(BLUE, 150)

        pyglow.update_leds()
        sleep(0.05)

        pyglow.set_leds(YELLOW, 0)
        pyglow.set_leds(GREEN, 25)
        pyglow.set_leds(BLUE, 50)
        pyglow.set_leds(WHITE, 150)

        pyglow.update_leds()
        sleep(0.05)

        pyglow.set_leds(GREEN, 0)
        pyglow.set_leds(BLUE, 25)
        pyglow.set_leds(WHITE, 50)

        pyglow.update_leds()
        sleep(0.05)

        pyglow.set_leds(BLUE, 0)
        pyglow.set_leds(WHITE, 25)

        pyglow.update_leds()
        sleep(0.05)

        pyglow.set_leds(WHITE, 0)

        pyglow.update_leds()
        sleep(0.05)

        #flash every LED three times
        for i in range(0, 2):
            pyglow.all(100)
            pyglow.all(0)
        

LEDFx1()
'''



        
