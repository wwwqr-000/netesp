class Menu:
    def __init__(self, name, items, frame, dictItemObj = "!"):#If dictItemObj is used, items is ignored
        self.name = name
        self.itemIndex = 0
        self.items = items
        self.frame = frame
        self.dictItemObj = dictItemObj

class Screen:
    def __init__(self, name, frame, textArr, callback, customCall = "!"):
        self.name = name
        self.frame = frame
        self.textArr = textArr
        self.callback = callback
        self.customCall = customCall