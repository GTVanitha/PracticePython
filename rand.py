import random

a= random.randint(1,9)

print "**You have enter a Guessing Game :) **"
user_inp = input("Enter a random number between 1 to 9.")

if (user_inp <  a):
    print "Your guess:%d is lesser than random number:%d" %(user_inp, a)
elif (user_inp > a):
    print "Your guess:%d is greater than random number:%d" %(user_inp, a)
else: 
    print "Woohoo!! You guessed it right!"
