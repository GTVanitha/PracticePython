import random

a = random.randint(1,9)

b = input('Enter a number between 1-9')

if ( a > b ):
    print ('>')
elif(a < b ):
    print('<')
else:
    print ('==')

print a,b 
