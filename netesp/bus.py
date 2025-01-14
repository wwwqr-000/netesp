from machine import I2C, Pin
from netesp import config
import _thread as thread
from time import sleep

rClickFunctions = []
lClickFunctions = []
enterFunctions = []

rBtn = Pin(config.rBtnPin, Pin.IN, Pin.PULL_UP)
lBtn = Pin(config.lBtnPin, Pin.IN, Pin.PULL_UP)
enter = Pin(config.enterBtnPin, Pin.IN, Pin.PULL_UP)


def keyListener():
    while True:
        sleep(0.01)
        if (rBtn.value() == 1): rBtnFunc()
        if (lBtn.value() == 0): lBtnFunc()
        if (enter.value() == 0): enterFunc()

def rBtnFunc():
    print("Right")

def lBtnFunc():
    print("Left")
    
def enterFunc():
    print("Enter")
    
thread.start_new_thread(keyListener, ())