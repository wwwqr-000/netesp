from netesp import menu, screen, wifi

menus = []#Menus contains Menu and Screen objects.
currentMenuName = "main"#The current name of a Menu or Screen object.
networkEntityList = {"entities": []}#A dictionary will dynamically update.
apLocIP = {"entities": [""]}#Contains the local IP-address of the esp32 while in ap-mode

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

    items = []
    if (menObj.dictItemObj == "!"): items = menObj.items
    else: items = menObj.dictItemObj["entities"]

    for i, e in enumerate(items):
        screen.drawTxt(e[0], 10, begin)
        begin += 10
        
    screen.refresh()
    arrowY = -2 + (10 * menObj.itemIndex)
    screen.drawIcon("arrow_left", 0, arrowY)
    screen.refresh()
    
def drawScreen(screenObj):
    if (screenObj == "!"):
        print("drawScreenInvalidObj")
        return
    
    global currentMenuName
    currentMenuName = screenObj.name
    
    begin = 12
    screen.cls()
    screen.drawFrame(screenObj.frame, 0, 0)
    if (len(screenObj.textArr) > 1):
        for i, e in enumerate(screenObj.textArr):
            screen.drawTxt(e, 10, begin)
            begin += 10
        
        screen.refresh()

    if (screenObj.customCall != "!"):#If menu's are something more unique, call their custom callback.
        func, arg = screenObj.customCall
        func(arg)

    
        
def menuIndexSwitch(inc):
    men = getMenuOrScreen(currentMenuName)
    if (men == "!" or isinstance(men, menu.Screen)): return
    index = men.itemIndex + inc

    items = []
    if (men.dictItemObj == "!"): items = men.items
    else: items = men.dictItemObj["entities"]

    if (index > (len(items) - 1) or index < 0): return
    men.itemIndex = index
    drawMenu(men)
    
def triggerItem(emptyArg):#For Screen and Menu obj's
    obj = getMenuOrScreen(currentMenuName)
    if (obj == "!"): return
    
    if (isinstance(obj, menu.Menu)):
        item = 0

        if (obj.dictItemObj == "!"): item = obj.items[obj.itemIndex]
        else: item = obj.dictItemObj["entities"][obj.itemIndex]

        itemName, payload = item
        callback, funcWArg = payload
        func, arg = funcWArg
        callback(func(arg))
    
    elif (isinstance(obj, menu.Screen)):
        callback, funcWArg = obj.callback
        func, arg = funcWArg
        callback(func(arg))

def getMenuCallback(menuName): return (drawMenu, (getMenuOrScreen, menuName))
def getScreenCallback(screenName): return (drawScreen, (getMenuOrScreen, screenName))

    
#Menu and Screen register
def register():
    scrn_credits = menu.Screen("scrn_credits", "credits", [], getMenuCallback("menu_main"))
    menu_main = menu.Menu("menu_main", [("Wifi", getMenuCallback("menu_wifi")), ("Bluetooth", getMenuCallback("menu_bluetooth")), ("ESPNow", getMenuCallback("menu_espnow")), ("Credits", getScreenCallback("scrn_credits"))], "gui")
    menu_wifi = menu.Menu("menu_wifi", [("Search", getScreenCallback("scrn_search")), ("Connect", getMenuCallback("menu_connect")), ("AccessPoint", getMenuCallback("menu_self_wifi_control")), ("Show IP's", (drawScreen, (getMenuOrScreen, "scrn_show_ips"))), ("Back", getMenuCallback("menu_main"))], "gui")
    scrn_search = menu.Screen("scrn_search", "gui", [], getMenuCallback("menu_wifi"), (wifi.showAvailable, "gui"))
    menu_connect = menu.Menu("menu_connect", [], "gui", networkEntityList)
    scrn_connect = menu.Screen("scrn_connect", "gui", ["W.I.P", "Keyboard..."], getMenuCallback("menu_wifi"))
    menu_self_wifi_control = menu.Menu("menu_self_wifi_control", [("Activate", getScreenCallback("scrn_swc_activate")), ("Deactivate", getScreenCallback("scrn_swc_deactivate")), ("Back", getMenuCallback("menu_wifi"))], "gui")
    scrn_swc_activate = menu.Screen("scrn_swc_activate", "gui", ["Activating..."], getMenuCallback("menu_self_wifi_control"), (wifi.toggleSelfWifiControl, True))
    scrn_swc_deactivate = menu.Screen("scrn_swc_deactivate", "gui", ["De-activating..."], getMenuCallback("menu_self_wifi_control"), (wifi.toggleSelfWifiControl, False))
    scrn_show_ips = menu.Screen("scrn_show_ips", "gui", [], getMenuCallback("menu_wifi"), (wifi.showIPs, "gui"))
    menus.append(menu_main)
    menus.append(scrn_credits)
    menus.append(menu_wifi)
    menus.append(scrn_search)
    menus.append(menu_connect)
    menus.append(scrn_connect)
    menus.append(menu_self_wifi_control)
    menus.append(scrn_swc_activate)
    menus.append(scrn_swc_deactivate)
    menus.append(scrn_show_ips)
#