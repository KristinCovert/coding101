# Exercise 3 (and Solution)

# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 

# OUR PLAN: ask user to give 10 numbers (check to see if it is an actual interger) - for each additional number at it to a list, then check the list to see if any of the numbers are less than 5

print ("\nLet's play a game!\n I'll ask for 10 numbers.")

list = []
counter = 0

while counter < 10:

	user_number = raw_input("Please give us a number:\n")
	
	try:
   			val = int(user_number)
   			list.append(user_number)
   			counter = counter + 1

	except ValueError:
   			print("That's not an int! Pleases use real numbers only.  That is REAL numbers from math class.")

print list

def get_less_than_value():
	
	start_value = raw_input("\nNow tell me a new number and I will tell you which one in your list are smaller. ")

	try:
		is_an_integer = int(start_value)
		
		###MAKE A NEW FUNCTION HERE TO SPLIT list based on less than - us a for loop

	except ValueError:
   		print("Soooo, remember we need real numbers here.  Try again!")
	 	get_less_than_value()

get_less_than_value()