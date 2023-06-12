# Raspberry Pi Pico RGB Blink
# rgb-blink.py

# RED LED - Pico GPIO 10 - Pin 14
# GREEN LED - Pico GPIO 11 - Pin 15
# BLUE LED - Pico GPIO 14 - Pin 19

import machine
import utime

led_red = machine.Pin(10, machine.Pin.OUT)
led_green = machine.Pin(11, machine.Pin.OUT)
led_blue = machine.Pin(14, machine.Pin.OUT)

while True:
    led_red.value(1)
    led_green.value(0)
    led_blue.value(0)
    utime.sleep(2)
    
    led_red.value(0)
    led_green.value(1)
    led_blue.value(0)
    utime.sleep(2)
    
    led_red.value(0)
    led_green.value(0)
    led_blue.value(1)
    utime.sleep(2)

    led_red.value(1)
    led_green.value(1)
    led_blue.value(0)
    utime.sleep(2)
    
    led_red.value(0)
    led_green.value(1)
    led_blue.value(1)
    utime.sleep(2)
    
    led_red.value(1)
    led_green.value(0)
    led_blue.value(1)
    utime.sleep(2)
    
    print("End of Loop")
    
    led_red.value(0)
    led_green.value(0)
    led_blue.value(0)
    utime.sleep(2)