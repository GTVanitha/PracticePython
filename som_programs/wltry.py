#! /usr/bin/env python

while 1:
	try:
	
		x = input("Enter 1st Number : ")
	except:
		print("Enter a Valid number")
		continue
	else:
		break
while 1:	
	try:
	
		y = input("Enter 2nd Number : ")
	except:
		print("Enter a Valid number")
		continue
	else:
		break
print x + y	
