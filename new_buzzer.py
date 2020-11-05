import time
import grovepi

buzzer = 3
 
grovepi.pinMode(buzzer,"OUTPUT")

def variable_delay_us(delay):
	int i = (delay + 5)/10
	while i != 0:
		time.sleep(0.00001)

def play_note(freq)
	period = 1000000/freq
	while freq != 0:
		grovepi.digitalWrite(buzzer,1)
		variable_delay_us(period/2)
		grovepi.digitalWrite(buzzer,0)
		variable_delay_us(period/2)

except KeyboardInterrupt:
		grovepi.digitalWrite(buzzer,0)
		break
	except IOError:
		print ("Error")