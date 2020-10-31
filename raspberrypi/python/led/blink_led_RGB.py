#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

green_led = 11
blue_led = 13
red_led = 15

GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
for x in range(0, 3):
    # Green LED
    print("Green")
    GPIO.output(green_led, True)
    GPIO.output(blue_led, False)
    GPIO.output(red_led, False)
    time.sleep(1)
    GPIO.output(green_led, False)
    time.sleep(.1)

    # Blue LED
    print("Blue")
    GPIO.output(blue_led, True)
    time.sleep(1)
    GPIO.output(blue_led, False)
    time.sleep(.1)

    # Red LED
    print("Red")
    GPIO.output(red_led, True)
    time.sleep(1)
    GPIO.output(red_led, False)
    time.sleep(.1)

    # Purple
    print("Purple")
    GPIO.output(blue_led, True)
    GPIO.output(red_led, True)
    time.sleep(1)
    GPIO.output(blue_led, False)
    GPIO.output(red_led, False)
    time.sleep(.1)
    
GPIO.cleanup()
