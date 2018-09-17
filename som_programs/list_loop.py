mylist = ['one', 'two', 'three', 'four', 'five']
for item in mylist:
    print item
    if(item == 'three'):
        break
s = ['h','e','l','l','o']   #create a list
s.append('d')               #append to end of list
print s,'d Added'
print len(s)                      #number of items in list
s.sort()                    #sorting the list
print s,'Hellod,Sorted'
s.reverse()                 #reversing the list
print s,'Reverse of Hellod'
s.extend(['w','o'])         #grow list
print s,'w o'
s.insert(1,2)               #insert into list
print s,'1 and 2'
s.remove('d')            #remove first item in list with value e
print s,'Remove d'
s.pop()                     #remove last item in the list
print s,'Pop?'
s.pop(1)                    #remove indexed value from list
print s,'POP1'
s.count('o')               #search list and return number of instances found
print s 
s = range(0,10)             #create a list over range 
print s
s = range(0,10,2)           #same as above, with start index and increment
print s

