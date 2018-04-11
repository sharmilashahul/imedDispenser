import RPi.GPIO as GPIO
from time import sleep
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
i=GPIO.input(3)
print(i)

motora = 7
motorb = 8 # Input Pin
motorc = 5  # Enable Pin

def set():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motora, GPIO.OUT)
    GPIO.setup(motorb, GPIO.OUT)
    GPIO.setup(motorc, GPIO.OUT)
    GPIO.setwarnings(False)

def backward():
    set()
    print"BACKWARD MOTION"
    GPIO.output(motora, GPIO.HIGH)
    GPIO.output(motorb, GPIO.LOW)
    GPIO.output(motorc, GPIO.HIGH)

def forward():
    set()
    print"FORWARD MOTION"
    GPIO.output(motora, GPIO.LOW)
    GPIO.output(motorb, GPIO.HIGH)
    GPIO.output(motorc, GPIO.HIGH)

def stop():
    set()
    print"STOP"
    GPIO.output(motorc, GPIO.LOW)

while True:
    i = GPIO.input(3)
    if i==1:
        forward()
        print "rotating",i
        time.sleep(0.5)
    if i==0:
        stop()
        print "stop",i
        time.sleep(0.5)
    else:
        forward()
        print "wait for input"



