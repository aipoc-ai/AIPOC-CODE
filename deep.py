import pygame.time
from pygame.mixer import *

pygame.mixer.init(frequency=800000)
filename = 'C:/Users/Deepanshu/Desktop/aipoc/voice.mp3'
music.load(filename)
music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)