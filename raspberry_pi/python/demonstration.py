#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

# Physical pins
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM)

# Power pins
# Ground = 6, 9, 14, 20, 25, 30, 34, 39
# 3.3V = 1, 17
# 5v = 2, 4

# Pin designators
pin1 = 3 # GPIO 2 (I2C1 SDA)
pin2 = 5 # GPIO 3 (I2C1 SCL)
pin3 = 7 # GPIO 4
pin4 = 8 # UART0 TX (can not be used as GPIO)
pin5 = 10 # UART0 RX (can not be used as GPIO)
pin6 = 11 # GPIO 17
pin7 = 12 # GPIO 18
pin8 = 13 # GPIO 27
pin9 = 15 # GPIO 22
pin10 = 16 # GPIO 23
pin11 = 18 # GPIO 24
pin12 = 19 # GPIO 10 (SPIO MOSI)
pin13 = 21 # GPIO 9 (SPIO MISO)
pin14 = 22 # GPIO 25
pin15 = 23 # GPIO 11 (SPIO SCLK)
pin16 = 24 # GPIO 8 (SPIO CS0)
pin17 = 26 # GPIO 7 (SPIO CS1)
pin18 = 29 # GPIO 5
pin19 = 31 # GPIO 6
pin20 = 32 # GPIO 12
pin21 = 33 # GPIO 13
pin22 = 35 # GPIO 19 (SPI1 MISO)
pin23 = 36 # GPIO 16 (SPI1 CS0)
pin24 = 37 # GPIO 26
pin25 = 38 # GPIO 20 (SPI1 MOSI)
pin26 = 40 # GPIO 21 (SPI1 SCLK)