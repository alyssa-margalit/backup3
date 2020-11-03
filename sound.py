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
from pygame import mixer
mixer.init()
mixer.music.load("forest.mp3")
mixer.music.play()
setText("hello")