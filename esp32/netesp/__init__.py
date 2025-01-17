from netesp import config, screen, bus, menu, keyRegistry
from time import sleep

bus.start()

screen.drawTxt("Loading...", 0, 0)
screen.refresh()

screen.cls()
screen.drawFrame("whiteavocado", 0, 5)
screen.cls()

menu.drawMain()
screen.refresh()

while True:
    sleep(0.1)
    print("marf")
