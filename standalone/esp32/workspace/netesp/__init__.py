from netesp import screen, bus, keyRegistry, superGlobal
from time import sleep

screen.drawTxt("Loading...", 0, 0)
screen.refresh()

screen.cls()
screen.drawFrame("whiteavocado", 0, 5)
screen.cls()

bus.start()
keyRegistry.register()
superGlobal.register()

superGlobal.drawMenu(superGlobal.getMenuOrScreen("menu_main"))
screen.refresh()

while True: sleep(0.1)
