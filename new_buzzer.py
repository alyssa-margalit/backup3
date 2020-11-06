import time
import grovepi

buzzer = 3
freq = 1000
i = 0
grovepi.pinMode(buzzer,"OUTPUT")

grovepi.analogWrite(buzzer, 262)
time.sleep(0.5)
grovepi.analogWrite(buzzer, 320)
time.sleep(0.5)
grovepi.analogWrite(buzzer, 440)
time.sleep(0.5)

grovepi.pinMode(buzzer,"INPUT")