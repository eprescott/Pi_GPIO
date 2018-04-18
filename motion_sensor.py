#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
PIR = 17
R_LED = 21
G_LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(R_LED,GPIO.OUT)
GPIO.setup(G_LED,GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)

current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(PIR)
        if current_state == 1:
            print("GPIO pin %s is %s" % (PIR, current_state))
            print("Motion Detected")
            GPIO.output(R_LED,GPIO.HIGH)
            GPIO.output(G_LED,GPIO.LOW)
            time.sleep(1)
            print("Motion clear")
            GPIO.output(R_LED,GPIO.LOW)
            GPIO.output(G_LED,GPIO.HIGH)
            time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

