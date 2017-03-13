# Exercise 3 (and Solution)

# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 

# OUR PLAN: ask user to give 10 numbers (check to see if it is an actual interger) - for each additional number at it to a list, then check the list to see if any of the numbers are less than 5

print ("Let's play a game, give ten numbers and I will tell you which ones are less than a certain number...")

list = []
counter = 0

while counter < 10:
	user_number = raw_input("Please give us a numnber:\n")
	list.append(user_number)
	counter = counter + 1
	print list