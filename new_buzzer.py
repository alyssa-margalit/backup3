import time
import grovepi

buzzer = 3
freq = 440
i = 0

while True:
	try: 
		if i < freq:
			grovepi.analogWrite(buzzer, i)
			i = i + 20
			time.sleep(0.5)


	except KeyboardInterrupt:
		grovepi.analogWrite(buzzer,0)
		break