import RPi.GPIO as GPIO          
from time import sleep
#for movement
in1 = 25
in2 = 14
in3=  22
in4= 23

def forward(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)    
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)
    sleep(x)
    GPIO.cleanup()
    
def backward(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.output(in2,True)
    GPIO.output(in3,True)
    sleep(x)
    GPIO.cleanup()

def rotate_r(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.output(in1,True)
    GPIO.output(in3,True)
    sleep(x)
    GPIO.cleanup()

def rotate_l(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in2,GPIO.HIGH)
    sleep(x)
    GPIO.cleanup()



backwARD(6)