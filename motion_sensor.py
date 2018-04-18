#!/usr/bin/env python

## Simple test of PIR sensor
# it will look for motion, when motion is detected it will print a 
# message to the screen and light a red LED. After PIR stops detecting 
# it will turn off the red light and light the green one.

# get GPIO library
import RPi.GPIO as GPIO
# get time library
import time

# set gpio pins for various components

# pasive IR sensor
PIR = 17
# Red LED
R_LED = 21
# Green LED
G_LED = 18

#setup GPIO modes and initalize GPIO Pins for use.
GPIO.setmode(GPIO.BCM)
GPIO.setup(R_LED,GPIO.OUT)
GPIO.setup(G_LED,GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)

# Set the current state for PIR to 0 not detecting
current_state = 0
try:

    # while True loop.
    while True:

	# pause for a 
        time.sleep(0.1)
	# get state from PIR
        current_state = GPIO.input(PIR)
        # If motion detected
	if current_state == 1:
            print("GPIO pin %s is %s" % (PIR, current_state))
            print("Motion Detected")
            GPIO.output(R_LED,GPIO.HIGH)
            GPIO.output(G_LED,GPIO.LOW)
            time.sleep(1)
	else:
            print("Motion clear")
            GPIO.output(R_LED,GPIO.LOW)
            GPIO.output(G_LED,GPIO.HIGH)
            time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

