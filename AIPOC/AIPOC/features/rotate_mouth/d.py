import RPi.GPIO as GPIO
#for setup

servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, False)
