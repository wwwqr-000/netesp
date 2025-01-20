#This file maps methods to key events trough the bus
from netesp import superGlobal, bus

def menuIndexUp(menuName): superGlobal.menuIndexSwitch(menuName, -1)
def menuIndexDown(menuName): superGlobal.menuIndexSwitch(menuName, 1)
            
def register():
    bus.rBtnFunctions.append((menuIndexUp, superGlobal.currentMenuName))
    bus.lBtnFunctions.append((menuIndexDown, superGlobal.currentMenuName))
    bus.enterFunctions.append((superGlobal.triggerMenuItem, superGlobal.currentMenuName))