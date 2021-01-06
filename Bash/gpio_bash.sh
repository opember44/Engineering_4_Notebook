#!/bin/bash

# GPIO Pins - Bash
# Written by Olivia Pemberton


gpio mode 0 out
gpio mode 27 out
# pin 17 and pin 16 as outputs
# in bash, 0 corresponds to pin 17, and 27 cooresponds to pin 16
# pin 17 has the green LED, pin 16 has the red LED

count=0
# counter starts at 0

while [ $count -lt 10 ];
# when the counter is less than 10:

do
# while loop starts

	gpio write 0 0
	gpio write 27 1
# first turns the pin 17 LED on and the pin 16 LED off

	sleep 1
# waits 2 second

	gpio write 0 1
	gpio write 27 0
# then turns the pin 17 LED off and the pin 16 LED on

	sleep 1
# waits another 2 seconds

	let count=count+1
# adds one to the counter

gpio write 0 0
# turns the pin 17 LED off

done
# indicates the end of the while loop

