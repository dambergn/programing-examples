import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# Connect to pin 12 not GPIO 12
servo = 12

GPIO.setup(servo, GPIO.OUT)

p = GPIO.PWM(servo, 50)
p.start(7.5)

try:
    while True:
        print "Move to Neutral"
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        print "move to 180"
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        print "move to 0"
        p.ChangeDutyCycle(2.5)
        time.sleep(1)

except KeyboardInterrupt:
    print "stopping program"
    p.stop()

    GPIO.cleanup()
