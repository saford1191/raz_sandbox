import RPi.GPIO as GPIO
import time

n = 23
t1 = 0.15
t2 = 0.275

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(n,GPIO.OUT)
print "LED on"
GPIO.output(n,GPIO.HIGH)
time.sleep(t1)
print "LED off"
GPIO.output(n,GPIO.LOW)
time.sleep(t2)
print "LED on"
GPIO.output(n,GPIO.HIGH)
time.sleep(t1)
print "LED off"
GPIO.output(n,GPIO.LOW)
time.sleep(t2)
print "LED on"
GPIO.output(n,GPIO.HIGH)
time.sleep(t1)
print "LED off"
GPIO.output(n,GPIO.LOW)
#time.sleep(t2)
