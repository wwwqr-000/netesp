from netesp import screen, superGlobal, config
import network
from time import sleep

class Entity:
    def __init__(self, name, mac, channel, sigStr, secLvl):
        self.name = name
        self.mac = mac
        self.channel = channel
        self.sigStr = sigStr
        self.secLvl = secLvl

def redrawScrnWFAT(frame, txt):#Redraw Screen With Frame And Text
    screen.cls()
    screen.drawFrame(frame, 0, 0)
    screen.drawTxt(txt, 10, 12)
    screen.refresh()

def showAvailable(frame):
    superGlobal.networkEntityList["entities"].clear()
    screen.cls()
    screen.drawFrame(frame, 0, 0)
    screen.drawTxt("Searching...", 10, 12)
    screen.refresh()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    sleep(2)

    networks = wlan.scan()
    yStart = 12
    screen.cls()
    screen.drawFrame(frame, 0, 0)
    for i, n in enumerate(networks):
        item = Entity(n[0].decode("utf-8"), n[1], n[2], n[3], n[4])
        tn = f"{ i + 1 }. { item.name }"
        screen.drawTxt(tn, 10, yStart)
        superGlobal.networkEntityList["entities"].append((tn[0:2], superGlobal.getScreenCallback("scrn_connect")))
        yStart += 10

    superGlobal.networkEntityList["entities"].append(("Back", superGlobal.getMenuCallback("menu_wifi")))
    screen.refresh()

def toggleSelfWifiControl(stat):
    ap = network.WLAN(network.AP_IF)
    ap.active(stat)
    if (not stat):
        superGlobal.apLocIP["entities"][0] = ""
        redrawScrnWFAT("gui", "De-Activated.")
        return

    ap.config(essid=config.selfWifiControlSSID, password=config.selfWifiControlPW, authmode=network.AUTH_WPA_WPA2_PSK)
    while not ap.active(): pass
    superGlobal.apLocIP["entities"][0] = str(ap.ifconfig()[0])
    redrawScrnWFAT("gui", "Activated.")

def showIPs(frame):
    screen.cls()
    screen.drawFrame(frame, 0, 0)
    res = superGlobal.apLocIP["entities"][0]
    if (res == ""): res = "none"
    screen.drawTxt(f"Private:", 10, 12)
    screen.drawTxt(res, 10, 22)
    screen.drawTxt("Public:", 10, 32)
    screen.drawTxt("none", 10, 42)
    screen.refresh()