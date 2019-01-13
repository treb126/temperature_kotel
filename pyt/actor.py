#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
from time import gmtime, strftime
butt_pin = 36
tim_on_h = 23#hour
tim_on_m = 30#minutes
tim_off_h = 6#hour
tim_off_m = 0#minutes
GPIO.setmode(GPIO.BCM)
GPIO.setup(butt_pin, GPIO.IN)
if GPIO.input(butt_pin) == True:

else:
	now_h = strftime("%H", gmtime())
	now_m = strftime("%M", gmtime())
	if h <  :
    	print('Low')
	elif -5 <= a <= 5:
    	print('Mid')
	else:
    	print('High')