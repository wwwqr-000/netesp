from machine import I2C, Pin
import ssd1306

i2c = I2C(0, scl=Pin(26), sda=Pin(25))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

maxWidth = 127
maxHeight = 63

def cls(): oled.fill(0)
def drawPixel(x, y, stat): oled.pixel(x, y, stat)
def drawTxt(txt, x, y): oled.text(txt, x, y)
def refresh(): oled.show()

def drawFrame(name):
    cls()
    f = open(f"netesp/frames/{ name }.frame", "r")
    for y, l in enumerate(f.readlines()):
        for x, c in enumerate(l):
            if (c == '1'): drawPixel(x, y, 1)
            else: drawPixel(x, y, 0)
    
    refresh()
    f.close()
