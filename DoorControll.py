# Script to open a chicken door.
# writen by Dorian Goettler, free to use unter the MIT licence.

# Requires: GPO, time.

import RPi.GPIO as GPIO
import time
import datetime
from suntime import Sun, SunTimeException



# Setup the gpio pins so that we can controll them. FOr this we are using pins 20 and 21.
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#This is the time in seconds that the door takes to open/close
TiemForDoorToClose = 10

def ChickenOpen:
    #spin the motor
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)

    # sleep timer
    time.sleep(TiemForDoorToClose)

    # Turn it off
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

def ChickenClose:
    #spin the motor
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)

    # sleep timer
    time.sleep(TiemForDoorToClose)

    # Turn it off
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)


#take a look at https://github.com/SatAgro/suntime for an idea how this works
latitude = 47.92
longitude = -122.21

Today_SunRise = sun.get_local_sunrise_time()
Today_Sunset = get_local_sunset_time 

#Now we go into a loop. We are checking every second to see if our condiotons are true, and if they are doing things
while exit = true
    if Today_SunRise = datetime.now()
        ChickenOpen()
    
    if Today_Sunset = datetime.now()
        #Give the chicks half an hour to get inside
        time.sleep (1800)
        ChickenClose()
        exit = false
    
    time.sleep(1)
