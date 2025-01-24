from machine import I2C, Pin
from netesp import config, ssd1306 

i2c = I2C(0, scl=Pin(config.screenSCL), sda=Pin(config.screenSDA))
oled = ssd1306.SSD1306_I2C(config.screenWidth + 1, config.screenHeight + 1, i2c)


def cls(): oled.fill(0)
def drawPixel(x, y, stat): oled.pixel(x, y, stat)
def drawTxt(txt, x, y): oled.text(txt, x, y)
def refresh(): oled.show()

def drawFrame(name, xOffset, yOffset):
    f = open(f"netesp/frames/{ name }.frame", "r")
    lines = f.readlines()
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if (c == '1'): drawPixel(x + xOffset, y + yOffset, 1)
    
    refresh()
    f.close()
    
def drawIcon(name, xOffset, yOffset, active = 1):
    f = open(f"netesp/icons/{ name }.icon", "r")
    for l in f.readlines():
        try:
            tmpArr = l.split(',')
            x = int(tmpArr[0]) + xOffset
            y = int(tmpArr[1]) + yOffset
            drawPixel(x, y, active)
        except Exception:
            print("Could not draw icon. Invalid format.")
            f.close()
            return
    
    refresh()
    f.close()

def displayYList(strList, marginleft):
    for i in range(50):
        yOffset = i
        cls()
        for l in strList:
            drawTxt(l, marginleft, yOffset)
            yOffset += 10
        refresh()