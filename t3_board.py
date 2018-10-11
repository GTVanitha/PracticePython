
print "Welcome to the world of Tic Tac Toe"

inp = input("What size game board you need to draw (3)/(5)/(8)?")



row=' --- '
col='|    '

i=0
while i < inp:
    print row*inp
    print col*(inp+1)
    i+=1
    

print row*inp



