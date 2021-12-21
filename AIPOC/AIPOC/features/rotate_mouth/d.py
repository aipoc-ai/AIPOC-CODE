import RPi.GPIO as GPIO
servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, False)
