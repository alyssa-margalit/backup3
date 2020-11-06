import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

red_led = 2
green_led = 3
blue_led = 4
button = 4
ranger = 3
buzzer = 2
potentiometer = 2
servoPIN = 17
fountain = 27

while True:
	try:
		pot = grovepi.analogRead(potentiometer)
		print(pot)
		time.sleep(1)
	except IOError:
		print("fail")