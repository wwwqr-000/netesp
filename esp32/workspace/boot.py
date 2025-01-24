from machine import I2C, Pin

f = open("netesp/config.py", "r")

exec(f.read())

editModeBtn = Pin(enterBtnPin, Pin.IN, Pin.PULL_UP)

if (editModeBtn.value() == 1): import netesp
