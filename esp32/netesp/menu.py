#This file contains some functions and variables to call all the menu's of netesp
from netesp import screen

current = "main"

mainIndex = 0
mainItems = ["Wifi", "Bluetooth", "Help", "Credits"]

def drawMain():
    begin = 12
    screen.cls()
    screen.drawFrame("gui", 0, 0)
    for i, e in enumerate(mainItems):
        screen.drawTxt(e, 10, begin)
        begin += 10
        
    screen.refresh()
    arrowY = -2 + (10 * mainIndex)
    screen.drawIcon("arrow_left", 0, arrowY)
    screen.refresh()
