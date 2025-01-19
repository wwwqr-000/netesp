#This file maps methods to key events trough the bus
from netesp import menu, bus

def menuIndexUp(): menu.changeMainMenuIndex("up")
def menuIndexDown(): menu.changeMainMenuIndex("down")
            
bus.rBtnFunctions.append(menuIndexUp)
bus.lBtnFunctions.append(menuIndexDown)