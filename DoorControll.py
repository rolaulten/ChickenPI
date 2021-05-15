#Script to open a chicken door.
#writen by Dorian Goettler, free to use unter the MIT licence.

#Requires: l298n, time.


from l298n import l298n
import time
motor1 = (20,21)

motor1.forwards
time.sleep(10)
motor1.stop