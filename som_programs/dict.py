months = { 1 : "January", 
                2 : "February", 
                        3 : "March", 
                                4 : "April", 
                                        5 : "May", 
                                                6 : "June", 
                                                        7 : "July",
                                                                8 : "August",
                                                                        9 : "September", 
                                                                        'b' : 2,
                                                                        'a': 1,
                                                                                10 : "October", 
                                                                                                12 : "December",
                                                                                                    11 : "November"}
print "===",months.keys()
print sorted(months)
i = 2
while True:
     if (i < 13):
         print months[i]
         i = i + 2
     else:
        break
s = months.keys();
s.sort()
print s

for i in months:
    if(type(i) == str):
        continue
    elif(i%2==0):
        print months[i]

