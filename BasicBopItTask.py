# Task:
# This is a beginner project to create an imitation of the classic bop it using the onboard LED and a buzzer as outputs, and
# buttons on the maker board for the inputs. You need to make it so there are three random outputs, and the player must push
# the correct corresponding button. The three output are LED On, Buzzer On, and LED and Buzzer On. You should randomise these
# outputs

#Bop It
from machine import Pin, PWM
from utime import sleep
import random

#Pins setup to work with the Maker Board
ledButton = Pin(20, Pin.IN, Pin.PULL_UP)
buzzButton = Pin(21, Pin.IN, Pin.PULL_UP)
bothButton = Pin(22, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(18))
buzzerFreq = 500
onBoardLED = Pin(25, Pin.OUT)
randomNum = random.randint(1,3)

def resetOutputs():
    #Turn both the LED and Buzzer Off
    sleep(0.5)

#You must remember to reset the random number
while True: 
    if randomNum == 1:
        #Turn the LED on, and then turn it off if the LED Button is pressed
    if randomNum == 2:
        #Turn the Buzzer on, and then turn it off if the Buzzer Button is pressed
    if randomNum == 3:
        #Turn the LED and Buzzer on, and then turn it off if the both Button is pressed.
    sleep(0.01)
    
    
# Extensions:
# Make it so if the players takes 5 seconds to react, they lose
# Add more outputs e.g. RGB LED with different colours, different frequency buzzers, add a voice telling you what to do like the real game!
# Add more inputs e.g. Shaking the pico, make a noise (requires extra hardware)
# Add a score system