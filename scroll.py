import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math

def scroll(the_text):
	str_pad = " "*16
	scroll_string = str_pad+the_text
	for i in range (0,len(scroll_string)):
		lcd_text = scroll_string[i:(i+15)]
		time.sleep(0.2)
		setText(lcd_text)
	setText(str_pad)


scroll("how dare you disturb my slumber")