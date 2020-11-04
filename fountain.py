import RPi.GPIO as GPIO           # import RPi.GPIO module 
import time 
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(4, GPIO.OUT) # set a port/pin as an output  
while True: 
	GPIO.output(4, 1)       # set port/pin value to 1/GPIO.HIGH/True
	time.sleep(10)
	GPIO.output(4, 0)       # set port/pin value to 0/GPIO.LOW/False  
	time.sleep(0)