# GPIO Pins - Python
# Written by Olivia Pemberton

from RPi.GPIO import setmode, setup, output, BCM, OUT, HIGH, LOW
# imports functions from the RPi.GPIO library

from time import sleep
# imports the sleep function from the time library

setmode(BCM)
# pins are called by the number on the pi

ledRED = 17
ledGREEN = 16
# red led is in GPIO pin 17
# green led is in GPIO pin 16

setup(ledRED, OUT)
setup(ledGREEN, OUT)
# sets led pins as outputs

count = 0
# counter starts at 0

while count < 10:
# until each led has blinked 10 times
	output(ledRED, HIGH)
	output(ledGREEN, LOW)
# turns the red led on (HIGH) and the green one off (LOW)
	sleep (1)
# pauses 1 second
	output(ledRED, LOW)
	output(ledGREEN, HIGH)
# turns the red led off and the green one on
	sleep (1)
# pauses another second
	count = count + 1
# adds one to the counter
output (ledGREEN, LOW)
# turns off the green led
