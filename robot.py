import RPi.GPIO as GPIO
from time import sleep

class Robot:
    def __init__(self, Motor1A, Motor1B, Motor2A, Motor2B):

        #Initialize instance variables
        self.Motor1A = Motor1A
        self.Motor1B = Motor1B
        self.Motor2A = Motor2A
        self.Motor2B = Motor2B
        
        #Set GPIO to use board pin numbers
        GPIO.setmode(GPIO.BOARD)

        #Turn GPIO warnings OFF
        GPIO.setwarnings(False)

        #Setup pins as outputs
        GPIO.setup(Motor1A, GPIO.OUT)
        GPIO.setup(Motor1B, GPIO.OUT)
        GPIO.setup(Motor2A, GPIO.OUT)
        GPIO.setup(Motor2B, GPIO.OUT)
	
	# Setup PWM output
	self.M1A = GPIO.PWM(Motor1A, 60)
	self.M1A.start(0)
	
	self.M1B = GPIO.PWM(Motor1B, 60)
	self.M1B.start(0)	

	self.M2A = GPIO.PWM(Motor2A, 60)
	self.M2A.start(0)

	self.M2B = GPIO.PWM(Motor2B, 60)
	self.M2B.start(0)

	
    def forward(self, speed=100):
        self.M1A.ChangeDutyCycle(speed)
        GPIO.output(self.Motor1B, GPIO.LOW)

        self.M2A.ChangeDutyCycle(speed)
        GPIO.output(self.Motor2B, GPIO.LOW)

    def backward(self, speed=100):
        GPIO.output(self.Motor1A, GPIO.LOW)
        self.M1B.ChangeDutyCycle(speed)

        GPIO.output(self.Motor2A, GPIO.LOW)
        self.M2B.ChangeDutyCycle(speed)

    def left(self, speed=100): 
        self.M1A.ChangeDutyCycle(speed)
        GPIO.output(self.Motor1B, GPIO.LOW)

        GPIO.output(self.Motor2A, GPIO.LOW)
        self.M2B.ChangeDutyCycle(speed)

    def right(self, speed=100):
        GPIO.output(self.Motor1A, GPIO.LOW)
        self.M1B.ChangeDutyCycle(speed)
        
	self.M2A.ChangeDutyCycle(speed)
        GPIO.output(self.Motor2B, GPIO.LOW)

    def stop(self):
        self.M1A.ChangeDutyCycle(0)
	self.M1B.ChangeDutyCycle(0)

	self.M2A.ChangeDutyCycle(0)
	self.M2B.ChangeDutyCycle(0)

    def cleanup(self):
        self.M1A.stop()
	self.M2A.stop()
	GPIO.cleanup()
	
