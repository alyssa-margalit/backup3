import time
import grovepi

potentiometer = 1

time.sleep(1)
pot = 0
while True:
	try: 
		pot = grovepi.analogRead(potentiometer)
		print(pot)
	except IOError:
		print("fail")
