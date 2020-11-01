import time 
import grovepi

buzzer = 6

grovepi.pinMode(buzzer, "OUTPUT")

def play_note(freq):

	period = 1000/freq
	while freq = freq - 1:
		grovepi.digitalWrite(buzzer, 1)
		time.sleep(1)
		grovepi.digitalWrite(buzzer, 0)
		time.sleep(1)

while True:
	play_note(440)