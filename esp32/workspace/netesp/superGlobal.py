from netesp import menu, screen

menus = []
currentMenuName = "main"

def getMenuOrScreen(menuName):
    for m in menus:
        if (m.name == menuName): return m
    
    return "!"

def drawMenu(menObj):
    global currentMenuName
    currentMenuName = menObj.name
    print(f"Drawing menu { currentMenuName }...")
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
    screen.drawFrame(screenObj.frame, 0, 0)
    for i, e in enumerate(screenObj.textArr):
        screen.drawTxt(e, 10, begin)
        begin += 10
    
    screen.refresh()
        
def menuIndexSwitch(inc):
    men = getMenuOrScreen(currentMenuName)
    if (men == "!" or isinstance(men, menu.Screen)): return
    index = men.itemIndex + inc
    if (index > (len(men.items) - 1) or index < 0): return
    men.itemIndex = index
    drawMenu(men)
    
def triggerItem(emptyArg):#For Screen and Menu obj's
    obj = getMenuOrScreen(currentMenuName)
    if (obj == "!"): return
    
    if (isinstance(obj, menu.Menu)):
        itemName, payload = obj.items[obj.itemIndex]
        callback, funcWArg = payload
        func, arg = funcWArg
        callback(func(arg))
    
    elif (isinstance(obj, menu.Screen)):
        callback, funcWArg = obj.callback
        func, arg = funcWArg
        callback(func(arg))
        
    
#Menu and Screen register
credits = menu.Screen("credits", "gui", ["test1", "test2"], (drawMenu, (getMenuOrScreen, "main")))
main = menu.Menu("main", [("Wifi", (drawMenu, (getMenuOrScreen, "wifi"))), ("Bluetooth", (drawMenu, (getMenuOrScreen, "bluetooth"))), ("Help", (drawScreen, (getMenuOrScreen, "help"))), ("Credits", (drawScreen, (getMenuOrScreen, "credits")))], "gui")
menus.append(main)
menus.append(credits)
#