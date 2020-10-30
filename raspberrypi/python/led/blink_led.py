#!/usr/bin/python3

# A simple GPIO high low blinking LED test.

import RPi.GPIO as GPIO
import time

# Physical pins
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM)

# Pin designators
green_led = 11

# Pin configuration
GPIO.setup(green_led, GPIO.OUT)

# set to False or 0 for on, True or 1 for off.
print("Turing LED on using False")
GPIO.output(green_led, False)
time.sleep(1)
print("Turing LED off using True")
GPIO.output(green_led, True)
time.sleep(1)
print("Turing LED on using 0")
GPIO.output(green_led, 0)
time.sleep(1)
print("Turing LED off using 1")
GPIO.output(green_led, 1)
time.sleep(1)

GPIO.cleanup()
