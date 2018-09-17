#! usr/bin/env python

"""x = input('Enter a Number : ')
i = 2
y = []

while i < x:
    if x%i==0:
        y.append(i)
    i = i + 1
if len(y)==0:
    print("Entered number is a not dividabale")
else:
    print(y)"""

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
        if num % number == 0:
                    divisorList.append(number)

                    print(divisorList)
