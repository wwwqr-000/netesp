#This file maps methods to key events trough the bus
from netesp import menu, bus

def changeMenuIndex(menuName, direction, drawFunc, menuItems):
    if (menu.current == menuName):
        itemCount = len(menuItems) - 1#Index based
        print(itemCount)
        if (direction == "up" and (menu.mainIndex - 1) <= itemCount):
            menu.mainIndex -= 1
            drawFunc()
        
        elif (direction == "down" and (menu.mainIndex + 1) <= itemCount):
            menu.mainIndex += 1
            drawFunc()
        

def menuIndexUp(): changeMenuIndex("main", "up", menu.drawMain, menu.mainItems)
def menuIndexDown(): changeMenuIndex("main", "down", menu.drawMain, menu.mainItems)
            
bus.rBtnFunctions.append(menuIndexUp)
bus.lBtnFunctions.append(menuIndexDown)