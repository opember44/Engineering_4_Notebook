# Python Program 3 - Strings and Loops
# Written by Olivia Pemberton

go = "y"
# defines the variable for while loop

print("After program is complete, press Enter to go again,")
print("press x then Enter to stop program")
# prints user instructions

while go == "y":
# this start the program
	sentence = input("Type your sentence, press enter when done: ")
# creates the sentance that the user typed
	splitsent = sentence.split()
# splits the sentence into an array of words atevery space
	for x in splitsent:

		letters = list (x)
# words are split into an array of letters
		for y in letters:
			print (y)
# each letter is printed on it own line
		print ("-")
# types - to represent a space 
	key = input(" ")
# user presses enter to continue 
	if key == "x":

		break
# program quits if x is pressed otherwise it restarts
