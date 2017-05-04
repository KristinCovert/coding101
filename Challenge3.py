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

# create a list and start a counter to get desired numbers

list = []
counter = 0

# ask for 10 numbers and add each one to the empty list

while counter < 10:

	user_number = raw_input("Please give a number:\n")
	
	try:
   			val = int(user_number)
   			list.append(int(user_number))
   			counter = counter + 1

   	# if the value entered is not a number remind people about MATH :)

	except ValueError:
   			print("\nThat's not an int! Pleases use real numbers only.  That is REAL numbers from math class.")

# Parot back the number list to the user

print ("\nThanks! Here are your numbers:%s" % (list))

# make a function that can judge which numbers in the list are less than a new value that the user gives

def get_less_than_value():
	
	# get the new value to determine which numbers are less than it

	start_value = raw_input("\nNow give a new number and I will tell you which number or numbers in your list are smaller. ")

	# to evaluate the numbers they have to be integers so make them so

	try:
		start_value = int(start_value)
	
	# if the number is not a interger let the user know to try again and recall the function to start again

	except ValueError:
   		print("\nSoooo, remember we need real numbers here.  Try again!")
	 	get_less_than_value()

	# create the list to hold the values less than

 	list_less_than = []

 	# evaluate each number and add it to the empty list

 	for values in list:

 		if values < start_value:
 			list_less_than.append(values)
 	
 	# print (list_less_than) - use to check if list built correctly

 	# using the length of list let the user know what numbers are less or if there are no numbers that are less than

	if len(list_less_than) < 1 :
		print("\nThere are no numbers in your list less than %s " % (start_value))

	elif len(list_less_than) > 1 :
		print (("\nThe numbers less than are: %s") % (list_less_than))
 		
get_less_than_value()
