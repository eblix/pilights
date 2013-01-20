import RPi.GPIO as GPIO
import time, math

x=0
while True:
	x = x+1

	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, True)
	time.sleep(0.15)

	GPIO.setup(8, GPIO.OUT)	
	GPIO.output(8, False)
	time.sleep(1)

        GPIO.setup(8, GPIO.OUT)
        GPIO.output(8, True)
        time.sleep(1)

        GPIO.setup(8, GPIO.OUT)
        GPIO.output(8, False)
        time.sleep(0.015)

