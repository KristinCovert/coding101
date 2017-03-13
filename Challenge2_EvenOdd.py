'''Odd Or Even 
input if types int equality comparison numbers mod
Again, the exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Exercise 2 (and Solution)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.'''

num = int(raw_input ("Wanna play even odd? Oh so glad you said yes.  Can you give me a number so I can tell you if it is odd or even, please? "))

def even_or_odd (num):
	if (num%2 == 0):
		print "Your number is EVEN!"

		if (num%4 ==0):
			print "Your number is also divisible by 4. Cool huh?"
	else:
		print "Your number is ODD!"

even_or_odd (num)

SMILE

