#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# Connect to pin 7 not GPIO 7
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)
p.start(7.5)

try:
    while True:
        print("Full Range Movement")
        print("Move to Neutral")
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        print("Move to 180")
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        print("Move to 0")
        p.ChangeDutyCycle(2.5)
        time.sleep(1)

        print("Precision Movements")
        print("Move to 18")
        p.ChangeDutyCycle(3.5)
        time.sleep(1)
        print("Move to 36")
        p.ChangeDutyCycle(4.5)
        time.sleep(1)
        print("Move to 54")
        p.ChangeDutyCycle(5.5)
        time.sleep(1)
        print("Move to 72")
        p.ChangeDutyCycle(6.5)
        time.sleep(1)

        print("Move to Neutral")
        p.ChangeDutyCycle(7.5)
        time.sleep(1)

        print("Move to 108")
        p.ChangeDutyCycle(8.5)
        time.sleep(1)
        print("Move to 126")
        p.ChangeDutyCycle(9.5)
        time.sleep(1)
        print("Move to 144")
        p.ChangeDutyCycle(10.5)
        time.sleep(1)
        print("Move to 162")
        p.ChangeDutyCycle(11.5)
        time.sleep(1)

        print("Move to 180")
        p.ChangeDutyCycle(12.5)
        time.sleep(1)

except KeyboardInterrupt:
    print("stopping program")
    p.stop()

    GPIO.cleanup()
