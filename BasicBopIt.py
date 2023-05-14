#Bop It
from machine import Pin, PWM
from utime import sleep
import random

ledButton = Pin(20, Pin.IN, Pin.PULL_UP)
buzzButton = Pin(21, Pin.IN, Pin.PULL_UP)
bothButton = Pin(22, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(18))
buzzerFreq = 500
onBoardLED = Pin(25, Pin.OUT)
randomNum = random.randint(1,3)

def resetOutputs():
    onBoardLED.value(0)
    buzzer.duty_u16(0)
    sleep(0.5)
    
while True: 
    if randomNum == 1:
        onBoardLED.value(1)
        if (ledButton.value() == 0):
            resetOutputs()
            randomNum = random.randint(1,3)
    if randomNum == 2:
        buzzer.duty_u16(1000)
        buzzer.freq(buzzerFreq)
        if (buzzButton.value() == 0):
            resetOutputs()
            randomNum = random.randint(1,3)
    if randomNum == 3:
        onBoardLED.value(1)
        buzzer.duty_u16(1000)
        buzzer.freq(buzzerFreq)
        if (bothButton.value() == 0):
            resetOutputs()
            randomNum = random.randint(1,3)
    sleep(0.01)
    
    
        