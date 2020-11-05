import time
import grovepi

buzzer = 3
 
length = 15
notes = "ccggaagffeeddc "
beats = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4]
tempo = 300;

def setup():
	grovepi.pinMode(buzzer,"OUTPUT")


def loop():

	for i in range(length):
		if notes[i] == ' ':
			delay(beats[i] * tempo)
		else:
			playNote(notes[i], beats[i] * tempo)
			delay(tempo / 2)



def playTone(tone, duration):
	step = 0
	end = duration * 1000
	for i in range (0, step, end):
		grovepi.digitalWrite(buzzer, 1)
		time.sleep(tone/100000)
		grovepi.digitalWrite(buzzer, 0)
		time.sleep(tone/100000)
		i += tone*2
		step = i


def playNote(note, duration) :
	char_names = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']
	tones = [1915, 1700, 1519, 1432, 1275, 1136, 1014, 956]
	step = 1
	for i in range(0, step, 8):
		if names[i] == note:
			playTone(tones[i], duration);
			step += 1

playNote(c, 1)