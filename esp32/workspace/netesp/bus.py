from machine import I2C, Pin
from netesp import config
import _thread as thread
from time import sleep

rBtnFunctions = []
lBtnFunctions = []
enterFunctions = []

rBtn = Pin(config.rBtnPin, Pin.IN, Pin.PULL_UP)
lBtn = Pin(config.lBtnPin, Pin.IN, Pin.PULL_UP)
enter = Pin(config.enterBtnPin, Pin.IN, Pin.PULL_UP)

rBtnCooldown = False
lBtnCooldown = False
enterCooldown = False


def keyListener():
    while True:
        sleep(0.01)
        if (rBtn.value() == 1):
            if (rBtnCooldown): continue
            rBtnCooldown = True
            for f in rBtnFunctions: f()
        
        else: rBtnCooldown = False

        if (lBtn.value() == 0):
            if (lBtnCooldown): continue
            lBtnCooldown = True
            for f in lBtnFunctions: f()

        else: lBtnCooldown = False

        if (enter.value() == 0):
            if (enterCooldown): continue
            enterCooldown = True
            for f in enterFunctions: f()

        else: enterCooldown = False
    
def start(): thread.start_new_thread(keyListener, ())