import time 
import grovepi

buzzer = 6

grovepi.pinMode(buzzer, "OUTPUT")
usleep = lambda x: time.sleep(x/1000000.0)

def play_note(freq):

	period = 1000/freq
	while True:
		grovepi.analogWrite(buzzer, 1)
		usleep(1700)
		grovepi.analogWrite(buzzer, 0)
		time.sleep(1700)
		

play_note(440)