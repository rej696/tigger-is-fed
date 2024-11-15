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

while not setup_network():
    print("Cannot connect!")

print("Connected!")

for i in range(5):
    try:
        time.sleep(5)
        set_time()
        print("Updated RTC")
        break
    except:
        print("Could not set RTC on boot")

tigger.main()
