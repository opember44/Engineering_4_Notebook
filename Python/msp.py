# Python Challenge - MSP Hangman
# Written by Olivia Pemberton

go = "y"
# defines the variable to start the while loop

while go == "y":
# starts the code

	print ("man-shaped pinata hangman game")
	phrase = input("enter your word to begin")
# user puts in the word that is going to be guessed by the other person
	print ("\n" * 50)
# this clears the screen
	words = phrase.split()
# uses an array spilts the phrases into words
	letters1 = []
	blanks = []
# empty arrays
	for x in words:

		letters = list (x)
# words are split into arrays of letters 
		wordlength = len(letters)
# word length is counted
		print ("__ " * wordlength, end = "   ")
# a black space is printed for each letter 
# prints a blank (3 spaces) between each word
 
		for x in letters:
# goes thru each letter
			letters1.append(x)
# stores each letter in a permanent array
			blanks.append ("_ ")
# adds a blank
		letters1.append ("  ")
		blanks.append ("  ")
# blanks are added after a word is finished
	wrong = 0

	runnums = []

	while wrong < 9:

		guess = input("\nPlayer 2, guess a letter or the answer: ")

		if guess in letters1:

			runcount = 0
# the array starts out having been searched 0 times
			for x in letters1:

				if x == guess:

					runnums.append (runcount)

				runcount = runcount + 1

			for x in runnums:

				blanks[x] = guess
# replaces the blank at that position with the guessed letter
			runnums.clear()
# clears the array
		if guess == phrase:
# if the user guesses the whole phrase
			c = 0

			for x in letters1:
				blanks[c] = x
				c = c + 1
# runs a loop
			wrong = wrong - 1
# cancels out the wrong guess count
		if guess not in letters1:
			wrong = wrong + 1
# wrong guess count increases by one
		for x in blanks:
			print (x, end = "")
# prints out the blanks array on one line
		if wrong >= 0:
			print ("\n_______")
			print ("       |")
			print ("       |")
		if wrong >= 1:
			print ("       0")
		if wrong >= 2:
			print ("       |")
		if wrong >= 3:
			print ("      /", end = "")
		if wrong >= 4:
			print ("|", end = "")
		if wrong >= 5:
			print ("\ ")
		if wrong >= 6:
			print ("       |")
		if wrong >= 7:
			print ("      /", end = "")
		if wrong >= 8:
			print (" \ ")
# for each wrong letter the program draws a line
		if wrong == 9:
			print ("GAME OVER - YOU LOSE, PLAYER 2")
			print ("The correct phrase was: ")
			print (phrase)
# the game end and the correct phrase is revealed
		if "_ " not in blanks:
                        print ("\nYOU WIN")
                        break

	again = input("play again? Enter Y or N: ")
	if again == "n":
		break
	print ("\n" * 50) 


