import RPi.GPIO as GPIO
import time, math

x=0
while True:
	x = x+1
	#sleeptime = 1+(math.sin(10*x/200.0))/36 % math.pi
	sinluv = 1+math.sin(10*x/200.0)
	sinluv2 = 1+math.sin(x)
	sleeptime = (sinluv / 30.) * sinluv2
	
	print "sleeptime is: %.6f (sinus: %.6f" % (sleeptime, sinluv)

	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, False)
	time.sleep(sleeptime)

	GPIO.setup(8, GPIO.OUT)	
	GPIO.output(8, True)
	time.sleep(sleeptime)
