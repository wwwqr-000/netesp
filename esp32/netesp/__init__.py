from netesp import config, screen, bus
from time import sleep

buff = ""

def left(): print("left")
def right(): print("right")
def enter():
    global buff
    
    print("enter")
    buff += "enter"

bus.lBtnFunctions.append(left)
bus.rBtnFunctions.append(right)
bus.enterFunctions.append(enter)

screen.drawTxt("Loading...", 0, 0)
screen.refresh()

screen.cls()
screen.drawFrame("whiteavocado")
sleep(1.5)

screen.cls()
screen.drawFrame("gui")

mainMenuItems = ["Menu item 1", "Menu item 2", "Menu item 3", "Menu item 4"]

yMenStart = 13
for i, e in enumerate(mainMenuItems):
    screen.drawTxt(e, 10, yMenStart)
    yMenStart += 10

screen.refresh()

while True:
    print("marf" + buff)
    sleep(0.2)
