import pygame
import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
pygame.mixer.init()
pygame.mixer.music.load('forest.mp3')
pygame.mixer.music.play(999)

setText("hello")