from netesp import loop, config, superGlobals
import _thread as thread
import network
from time import sleep

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.wifiSSID, config.wifiPW)
while not wlan.isconnected(): pass
superGlobals.IP["entities"].append(wlan.ifconfig()[0])

thread.start_new_thread(loop.main, ())
while True: sleep(1)