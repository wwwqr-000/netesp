from netesp import config, screen, bus, menu, keyRegistry, superGlobal
from time import sleep

screen.drawTxt("Loading espnet...", 0, 0)
screen.refresh()

screen.cls()
screen.drawFrame("whiteavocado", 0, 5)
screen.cls()

bus.start()
keyRegistry.register()

superGlobal.drawMenu(superGlobal.getMenuOrScreen("main"))
screen.refresh()

while True: sleep(0.1)
