#! /usr/bin/env python
name = raw_input("Enter your name : ")
while 1:

	try:
	 age = input("Enter your age : ")
	except :
		print("enter a valid age : ")
		continue
	else :
		break
x = 100 - age
if ( age > 100):
	print ( " You are more than 100 years old")
else :
	print (" Your will turn 100 in %d years") %(x)


