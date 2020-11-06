import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

red_led = 2
green_led = 3
blue_led = 4
button = 4
ranger = 3
buzzer = 2
potentiometer = 2
servoPIN = 17
fountain = 27

#set up buzzer and button
grovepi.pinMode(buzzer, "OUTPUT")
grovepi.pinMode(button, "INPUT")

#set up the motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(2.5)

#set up the fountain
GPIO.setup(fountain, GPIO.OUT) # set a port/pin as an output  
GPIO.output(fountain, 1)       # set port/pin value to 1/GPIO.HIGH/True

#set up the LEDs
GPIO.setup(red_led, GPIO.OUT) # set a port/pin as an output  
GPIO.output(red_led, 0)       # set port/pin value to 1/GPIO.HIGH/True
GPIO.setup(green_led, GPIO.OUT) # set a port/pin as an output  
GPIO.output(green_led, 1)       # set port/pin value to 1/GPIO.HIGH/True
GPIO.setup(blue_led, GPIO.OUT) # set a port/pin as an output  
GPIO.output(blue_led, 0)       # set port/pin value to 1/GPIO.HIGH/True

print("pin initialization complete")



#function to scroll text on lcd
def scroll(the_text):
	str_pad = " "*16
	scroll_string = str_pad+the_text
	for i in range (0,len(scroll_string)):
		lcd_text = scroll_string[i:(i+15)]
		time.sleep(0.1)
		setText(lcd_text)
	setText(str_pad)




#callback to get a question from the vm from the API
def trivia_question_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	global question 
	question = str(message.payload, "utf-8")
	print(question)

#callback to get the answer from the vm from the API
def trivia_answer_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	global answer
	answer = str(message.payload, "utf-8")
	print(answer)
	


#subscribe to getting the question and answer
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("alyssasrpi/trivia_question")
    client.message_callback_add("alyssasrpi/trivia_question", trivia_question_callback)
    client.subscribe("alyssasrpi/trivia_answer")
    client.message_callback_add("alyssasrpi/trivia_answer", trivia_answer_callback)
    print("connected")


#Default message callback. 
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))



if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	client.loop_start()

	
	story = 0

	while True: 
		print("things")
		pot = grovepi.analogRead(potentiometer)
		print(pot)
		time.sleep(1)


			

				
			



