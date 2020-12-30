# Automatic Dice Roller
# Written by Olivia Pemberton

from random import randint

go = "y"

print ("Automatic Dice Roller")
print ("Press enter to roll")
print ("Press X then enter to quit")

while go == "y":
	key = input (" ")

	if key == "x":

		break

	print (randint (1, 6))
