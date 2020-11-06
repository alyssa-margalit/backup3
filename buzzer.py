import time 
import grovepi

buzzer = 6

grovepi.pinMode(buzzer, "OUTPUT")
usleep = lambda x: time.sleep(x/1000000.0)

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
		usleep(1700)
		grovepi.analogWrite(buzzer, 0)
		time.sleep(1700)
		
>>>>>>> d040793e2274c8a2df4398e2540e73bf23866159


play_note(440)

except KeyboardInterrupt: 
	grovepi.digitalWrite(buzzer, 0)
	break