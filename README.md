# TIGGER HAS BEEN FED FOR NOW!!

micropython scripts for using pi pico w, pimoroni display pack 2 and ntp to display a message saying tigger has or has not been fed.

It will reset the fed status at predefined times.

It connects to the internet, updates the RTC with ntp, and then loops looking for button presses. if a button is pressed, it will update the message on the screen to indicate tigger has been fed. If the time hits a predefined value, it will reset the message to indicate tigger is hungry

```
rshell
cp *.py /pyboard/
```

## links
https://blog.martinfitzpatrick.com/using-micropython-raspberry-pico/
https://www.tomshardware.com/how-to/connect-raspberry-pi-pico-w-to-the-internet
https://github.com/benevpi/pico_w_micropython_simple_ntp/blob/main/simple_ntp.py
https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_display/rainbow.py
