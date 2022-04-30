import RPi.GPIO as GPIO
import time
#for servomoter
servoPIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, False)

p = GPIO.PWM(servoPIN, 50) # GPIO 16 for PWM with 50Hz
p.start(5) # Initialization

p.ChangeDutyCycle(4)
time.sleep(0.5)
p.ChangeDutyCycle(5)
time.sleep(0.5)
p.ChangeDutyCycle(6)
time.sleep(0.5)
p.ChangeDutyCycle(7)
time.sleep(0.5)
p.ChangeDutyCycle(7.5) #mid
time.sleep(0.5)
p.ChangeDutyCycle(8)
time.sleep(0.5)
p.ChangeDutyCycle(9)
time.sleep(0.5)
p.ChangeDutyCycle(10)
time.sleep(0.5)
p.ChangeDutyCycle(9)
time.sleep(0.5)
p.ChangeDutyCycle(8)
time.sleep(0.5)
p.ChangeDutyCycle(7) #mid
time.sleep(0.5)
p.ChangeDutyCycle(6)
time.sleep(0.5)
p.ChangeDutyCycle(5)
time.sleep(0.5)
p.ChangeDutyCycle(4)
time.sleep(0.5)

p.stop()
GPIO.cleanup()

