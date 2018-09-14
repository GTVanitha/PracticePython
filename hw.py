#! /usr/bin/env python

""" Sample two number 
python script
"""

print "Arithmetic operations";
while True:
    try:
        x = int(input("Enter first number:"))
        y = int(input("Enter second number:"))
    except:
        print "**Enter digit as input**"
        continue
    else:
        break

print "Addition(", x ,"+", y, "):", x + y 
print "Sub(", x ,"-", y, "):", x - y 
print "Multiply(", x ,"*", y, "):", x * y 
print "Division(", y ,"/", x, "):",  y / x
