import time
import grovepi
from grovepi import *



potentiometer = 1
button = 4
pinMode(button ,"INPUT")

time.sleep(1)
pot = 0
while True:
	try: 
		pot = grovepi.analogRead(potentiometer)
		print(pot)
		status = digitalRead(button)
		if status:
			print("pressed")

	except IOError:
		print("fail")
