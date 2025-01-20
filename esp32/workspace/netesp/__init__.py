from netesp import config, screen, bus, menu, keyRegistry, superGlobal
from time import sleep

bus.start()

screen.drawTxt("Loading test...", 0, 0)
screen.refresh()

screen.cls()
screen.drawFrame("whiteavocado", 0, 5)
screen.cls()

superGlobal.drawMenu(superGlobal.getMenu("main"))
screen.refresh()

while True: sleep(0.1)
