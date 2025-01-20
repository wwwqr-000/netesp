class Menu:
    def __init__(self, name, items, frame):
        self.name = name
        self.itemIndex = 0
        self.items = items
        self.frame = frame

class Screen:
    def __init__(self, name, frame, textArr, callback):
        self.name = name
        self.frame = frame
        self.textArr = textArr
        self.callback = callback