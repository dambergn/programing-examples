#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

servoPin = 7
GPIO.setup(servoPin, GPIO.OUT)

pwm = GPIO.PWM(servoPin, 50)
# pwm=GPIO.PWM(servoPin,300)

pwm.start(7.5)
# speed=.0025
speed = .01


try:
    while True:
        for i in range(0, 180):
            DC = float(1/18)*float(i)+2
            pwm.ChangeDutyCycle(DC)
            time.sleep(speed)
        print("Forward")

        for j in range(180, 0, -1):
            DC = float(1/18)*float(j)+2
            pwm.ChangeDutyCycle(DC)
            time.sleep(speed)
        print("Reverse")

except KeyboardInterrupt:
    print("Stopping Program")
    pwm.stop()
    GPIO.cleanup()
