import time 
import grovepi

buzzer = 6

grovepi.pinMode(buzzer, "OUTPUT")

def variable_delay_us(delay):
	int i = (delay + 5)/10
	while i != 0:
		time.sleep(0.1)

def play_note(freq):

	period = 1000/freq
	while freq != 0:
		grovepi.analogWrite(buzzer, 1)
		variable_delay_us(period/2)
		grovepi.analogWrite(buzzer, 0)
		variable_delay_us(period/2)
		freq = freq - 1


play_note(440)

except KeyboardInterrupt: 
	grovepi.digitalWrite(buzzer, 0)
	break