import network
import secrets
import time

def setup_network():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    print(wlan.isconnected())
