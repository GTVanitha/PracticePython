def changeme(mylis):
    #mylis.append(4)
    #mylis.append(5)
    mylis = [7,8,9]
    return

mylist = [1,2,3]

print "before fucntion call", mylist

changeme(mylist)

print "After function call", mylist



# variable 
a=1

def change(a, b, *c):
    print "a:", a
    print "b:",b
    d = []
    for i in c:
        d.append(i)
    print c[0]
    print d
    return

change(1, 2, 4,5,6)

