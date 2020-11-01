import time 
import grovepi

buzzer = 6

grovepi.pinMode(buzzer, "OUTPUT")

def play_note(freq):

	period = 1000/freq
	while True:
		grovepi.analogWrite(buzzer, 1)
		time.sleep(1)
		grovepi.analogWrite(buzzer, 0)
		time.sleep(1)
		freq = freq - 1

play_note(440)