import time
import grovepi
from grovepi import *
import math


potentiometer = 1
button = 4
pinMode(button ,"INPUT")

#time.sleep(1)
#pot = 0
while True:
	try: 
		print("here")
		pot = grovepi.analogRead(potentiometer)
		print(pot)
		status = digitalRead(button)
		if status:
			print("pressed")
		time.sleep(1)

	except IOError:
		print("fail")
