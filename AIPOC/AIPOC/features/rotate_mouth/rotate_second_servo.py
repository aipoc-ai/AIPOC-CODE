import RPi.GPIO as GPIO
import time

servoPIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 20 for PWM with 50Hz
p.start(5) # Initialization
p.ChangeDutyCycle(4)
time.sleep(1)
p.ChangeDutyCycle(6)
time.sleep(1)
p.ChangeDutyCycle(7)
time.sleep(1)
p.ChangeDutyCycle(8)
time.sleep(1)
p.ChangeDutyCycle(9)
time.sleep(1)
p.ChangeDutyCycle(10)
time.sleep(1)
p.ChangeDutyCycle(9)
time.sleep(1)
p.ChangeDutyCycle(8)
time.sleep(1)
p.ChangeDutyCycle(7)
time.sleep(1)
p.ChangeDutyCycle(6)
time.sleep(1)
p.ChangeDutyCycle(2)
time.sleep(1)
p.stop()
GPIO.cleanup()
