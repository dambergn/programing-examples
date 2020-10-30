#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

green_led = 11
blue_led = 13
red_led = 15

GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
for x in range(0, 7):
    GPIO.output(green_led, True)
    time.sleep(.5)
    GPIO.output(green_led, False)
    GPIO.output(blue_led, True)
    time.sleep(.5)
    GPIO.output(blue_led, False)
    GPIO.output(red_led, True)
    time.sleep(.5)
    GPIO.output(red_led, False)
GPIO.cleanup()
