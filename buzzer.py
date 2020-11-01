import time 
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()

my_buzzer = gpg.init_buzzer("AD2")

my buzzer.sound(440)

time.sleep(1)

my_buzzer.sound(880)

time.sleep(1)

my_buzzer.sound(220)

time.sleep(1)