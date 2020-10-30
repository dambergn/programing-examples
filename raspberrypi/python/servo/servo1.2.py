#!/usr/bin/python3

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Connect to pin 12 not GPIO 12
servo = 12

GPIO.setup(servo, GPIO.OUT)

pwm = GPIO.PWM(servo, 50)

pwm.start(7.5)

for i in range(0, 20):
    desiredPosition = input("Where do you want the servo to go?(9 - 180) ")
    DC = float(1/18)*float(desiredPosition)+2
    pwm.ChangeDutyCycle(DC)

# while(1):
#     # Servo movement
#     position=input("How far do you want to move the servo?(2.5 - 12.5) ")
#     pwm.ChangeDutyCycle(float(position))

pwm.stop()
GPIO.cleanup()
