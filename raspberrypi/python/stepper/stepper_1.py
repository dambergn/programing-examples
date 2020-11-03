#!/usr/bin/python3
# This code completes a 48 step rotation with high torque

from time import sleep
import RPi.GPIO as GPIO

DIR = 11 # Direction GPIO Pin
STEP = 7 # STEP GPIO Pin
CW = 1   # Clockwise Rotation
CCW = 0  # Couterclockwise Rotation
SPR = 48 # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = .0208

print("Forward")

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)

print("Reverse")

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

print("Done")
GPIO.cleanup()
