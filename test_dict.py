months = { 1 : "January", 
        2 : "February", 
        3 : "March", 
        4 : "April", 
        5 : "May", 
        6 : "June", 
        7 : "July",
        8 : "August",
        9 : "September", 
        10 : "October", 
        11 : "November",
        'a':1,
        12 : "December" 
        } 

for m in months:
    if (type(m) == str):
        continue
    if (m%2 == 0) :
        print months[m]


for m,n in months.items():
    print "key:", m, "Value:", n

print "lebngth: ", len(months)
# delete all kv pairs
months.clear()

print months

# length is asme as list
print "lentgh", len(months)
