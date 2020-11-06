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

#set up buzzer and button
grovepi.pinMode(buzzer, "OUTPUT")
grovepi.pinMode(button, "INPUT")

#set up the motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(2.5)

#set up the fountain
GPIO.setup(fountain, GPIO.OUT) # set a port/pin as an output  
GPIO.output(fountain, 1)       # set port/pin value to 1/GPIO.HIGH/True

#set up the LEDs
GPIO.setup(red_led, GPIO.OUT) # set a port/pin as an output  
GPIO.output(red_led, 0)       # set port/pin value to 1/GPIO.HIGH/True
GPIO.setup(green_led, GPIO.OUT) # set a port/pin as an output  
GPIO.output(green_led, 1)       # set port/pin value to 1/GPIO.HIGH/True
GPIO.setup(blue_led, GPIO.OUT) # set a port/pin as an output  
GPIO.output(blue_led, 0)       # set port/pin value to 1/GPIO.HIGH/True

print("pin initialization complete")



