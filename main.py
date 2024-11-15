import time
import network
import secrets
import machine
import tigger
from ntp import set_time

def setup_network():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # wlan.connect("Woodlands-mycelium", "have-a-good-day")
    wlan.connect(secrets.SSID, secrets.PASSWORD)
    time.sleep(5)
    return wlan.isconnected()

def pico_print(text):
    print(text)
    tigger.display.set_pen(tigger.BLACK)
    tigger.display.clear()
    tigger.display.set_pen(tigger.WHITE)
    tigger.display.text(text, 10, 10, 240, 6)

connected = False
while not connected:
    try:
        connected = setup_network()
        if not connected:
            pico_print("Connection Error!")
    except:
        time.sleep(5)
        pico_print("Connection Error!")

pico_print("Connected!")

for i in range(5):
    try:
        time.sleep(5)
        set_time()
        pico_print("Updated RTC")
        break
    except:
        pico_print("Could not set RTC on boot")

tigger.main()
