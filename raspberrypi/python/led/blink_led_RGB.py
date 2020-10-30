#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

green_led = 11
blue_led = 13
red_led = 15

GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)
for x in range(0, 7):
    # Green LED
    GPIO.output(green_led, True)
    time.sleep(.5)
    GPIO.output(green_led, False)
    time.sleep(.1)

    # Blue LED
    GPIO.output(blue_led, True)
    time.sleep(.5)
    GPIO.output(blue_led, False)
    time.sleep(.1)

    # Red LED
    GPIO.output(red_led, True)
    time.sleep(.5)
    GPIO.output(red_led, False)
    time.sleep(.1)
GPIO.cleanup()
