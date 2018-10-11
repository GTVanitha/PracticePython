import random

n = random.sample('1234567890',4)
print n

counter = 0

def cow_bull(msg):

    #global counter
    #counter += 1
    globals()['counter'] += 1

    #print globals()['counter']

    #print "gloabls:", globals()
    #print "local:", locals()

    while True:
        #i = map( str, raw_input("Enter 4 digit to compare with computer pic : "))
        i = raw_input("Enter 4 digit to compare with computer pic : ")
        if (len(i))<> 4:
           print("Please enter 4 digit numbers only :")
           continue
        else:
           break
    
    
    print i
    cow = 0
    bull = 0
    b = 0
    for a in n:
      if a == i[b]:
        cow = cow + 1
        b = b + 1
      elif a in i:
        bull = bull + 1
        b = b + 1
    
    print cow,bull

    if cow == len(n):
        print "you have tried %d times." %(counter) 
        print "You won!"
    else:
        cow_bull(msg = 'Try again..')

cow_bull(msg = 'Welcome to Cows and Bulls game')
