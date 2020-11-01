import RPi.GPIO as GPIO
import time 
import grovepi

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER = 6
grovepi.pinMode(BUZZER, "OUTPUT")
GPIO.setup(BUZZER, GPIO.OUT)

def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       grovepi.digitalWrite(BUZZER, 1)
       time.sleep(halveWaveTime)
       grovepi.digitalWrite(BUZZER, 0)
       time.sleep(halveWaveTime)
def play():
    t=0
    notes=[262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262]
    duration=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,1,0.25,0.25,0.25,0.25,0.5,0.5,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,1,0.5,0.5,1]
    for n in notes:
        buzz(n, duration[t])
        time.sleep(duration[t] *0.1)
        t+=1
#buzz(262, 0.5)

play()