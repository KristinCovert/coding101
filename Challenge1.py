# coding= UTF-8   
### Command line of python <filename> was getting angry till I added the line above. I think ### it  needs to know what types of characters to expect (i.e. latin, korean, etc..)
import datetime

### I needed to switch to single quotes instead of double. I’m not sure why...
name = raw_input('Yo what yo name sucka? ')
age = int(raw_input('Just how ancient are you? '))
now = datetime.datetime.now()

#calculate when a person will be 100 years old by taking the 
#current year, subtracting their current age then adding 100 
#years.

def year_when_99(age):
	when_you_will_be_99 = now.year - age + 99
	return when_you_will_be_99
### The line below would not work until I put the variable answer before the function. From a 
### computer’s mind, reading code left to right it will identify that there is an ‘empty’ variable 
### named answer and oh okay we are going to run this function and put the returned result ### in it
answer = year_when_99(age)

print "%s, you will be 100 years old in the year %s\n" % (name, answer) 

rub_it_in_num = int(raw_input('Give me a number, old fart? '))

print "%s, you will be 100 years old in the year %s\n" % (name, answer) * rub_it_in_num




