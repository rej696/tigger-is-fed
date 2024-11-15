import time
import machine

from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY_2, PEN_RGB565
from pimoroni import RGBLED, Button

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY_2, pen_type=PEN_RGB565, rotate=0)
display.set_backlight(0.8)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()
BLACK = display.create_pen(0, 0, 0)

# what size steps to take around the colour wheel
OFFSET = 0.0025


# From CPython Lib/colorsys.py
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

FEED_ME = "TIGGER IS HUNGRY, PLEASE FEED ME!!"
FULL =    "TIGGER HAS BEEN FED, FOR NOW..."

def main():
    tigger_text = FEED_ME
    counter = 0
    # variable to keep track of the hue
    h = 0.0
    while True:
        if button_a.read() or button_b.read() or button_x.read() or button_y.read():
            tigger_text = FULL

        if counter < 50:
            counter += 1
            continue

        counter = 0

        current_time = machine.RTC().datetime()
        hour, minute, second = current_time[4], current_time[5], current_time[6]
        if hour == 12 and minute == 0:
            set_time()

        if hour == 6 and minute == 1:
            tigger_text = FEED_ME

        if hour == 16 and minute == 31:
            tigger_text = FEED_ME

        # increment the hue each time round the loop
        h += OFFSET

        RAINBOW = display.create_pen_hsv(h, 1.0, 1.0)
        display.set_pen(RAINBOW)
        display.clear()

        # Draw some black text
        display.set_pen(BLACK)
        display.text(tigger_text, 10, 10, 240, 6)

        display.update()

        time.sleep(0.1)
