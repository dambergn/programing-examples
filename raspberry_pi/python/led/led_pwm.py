#!/usr/bin/python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
blue_led = 7
GPIO.setup(blue_led, GPIO.OUT)
my_pwm = GPIO.PWM(blue_led, 100)
my_pwm.start(100)
while(1):
    # 100 for off to 0 for brightest
    bright = input("How bright do you want the LED?(0 - 100) ")
    my_pwm.ChangeDutyCycle(float(bright))

    # 10 for lowest to 1 for highest
    # bright=input("How bright do you want the LED?(1-6) ")
    # my_pwm.ChangeDutyCycle(2**float(bright))

my+pwm.stop()
GPIO.cleanup()
