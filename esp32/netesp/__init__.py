from netesp import config, screen, bus
from time import sleep

def test(): print("test")

bus.enterFunctions.append(test)

screen.drawTxt("Test", 0, 0)
screen.refresh()

screen.drawFrame("welcome")

while True:
    print("marf")
    sleep(0.2)
