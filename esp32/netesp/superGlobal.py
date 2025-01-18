from netesp import menu, screen

menus = []
main = menu.Menu("main", ["Wifi", "Bluetooth", "Help", "Credits"])
menus.append(main)

def getMenu(menuName):
    for m in menus:
        if (m.name == menuName): return m
    
    return "!"

def drawMenu(menObj):
    begin = 12
    screen.cls()
    screen.drawFrame("gui", 0, 0)
    for i, e in enumerate(menObj.items):
        screen.drawTxt(e, 10, begin)
        begin += 10
        
    screen.refresh()
    arrowY = -2 + (10 * menObj.itemIndex)
    screen.drawIcon("arrow_left", 0, arrowY)
    screen.refresh()

def changeMenuIndex(menuName, direction):
    global menus
    
    for m in menus:
        print(m.name)