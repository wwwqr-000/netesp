from netesp import menu, screen

menus = []
currentMenuName = "main"

def getMenu(menuName):
    for m in menus:
        if (m.name == menuName): return m
    
    return "!"

def getScreen(screenName):
    for s in menus:
        if (s.name == screenName): return s
        
    return "!"

def drawMenu(menObj):
    global currentMenuName
    currentMenuName = menObj.name
    begin = 12
    screen.cls()
    screen.drawFrame(menObj.frame, 0, 0)
    for i, e in enumerate(menObj.items):
        screen.drawTxt(e[0], 10, begin)
        begin += 10
        
    screen.refresh()
    arrowY = -2 + (10 * menObj.itemIndex)
    screen.drawIcon("arrow_left", 0, arrowY)
    screen.refresh()
    
def drawScreen(screenObj):
    global currentMenuName
    currentMenuName = screenObj.name
    
    begin = 12
    screen.cls()
    screen.drawFrame(screenObj.frame)
    for i, e in enumerate(screenObj.textArr):
        screen.drawTxt(e, 10, begin)
        begin += 10
    
    screen.refresh()
        
def menuIndexSwitch(menuName, inc):
    men = getMenu(menuName)
    if (men == "!"): return
    index = men.itemIndex + inc
    if (index > (len(men.items) - 1) or index < 0): return
    men.itemIndex = index
    drawMenu(men)
    
def triggerMenuItem(menuOrScreenName):#For Screen and Menu obj's
    men = getMenu(menuOrScreenName)
    if (men != "!"):
        itemName, payload = men.items[men.itemIndex]
        callback, funcWArg = payload
        func, arg = funcWArg
        callback(func(arg))
    
    else:
        scrn = getScreen(menuOrScreenName)
        if (scrn == "!"): return
        callback, funcWArg = scrn.callback
        func, arg = funcWArg
        callback(func(arg))
    
#Menu and Screen register
credits = menu.Screen("credits", "gui", ["test1", "test2"], (drawMenu, (getMenu, "main")))
main = menu.Menu("main", [("Wifi", (drawMenu, (getMenu, "wifi"))), ("Bluetooth", (drawMenu, (getMenu, "bluetooth"))), ("Help", (drawScreen, (getScreen, "help"))), ("Credits", (drawScreen, (getScreen, "credits")))], "gui")
menus.append(main)
menus.append(credits)
#