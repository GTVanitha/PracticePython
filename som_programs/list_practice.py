#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
#i = len(a)
#
#s = input("Enter the limit : ")
#b = []
#
#while i >= 0:
#        i=i-1
#        if( a[i] <= s):
#            b.append(a[i])
#        continue
#print b
        
# print all the elements which is less than 5, in one line code
#print [aa for aa in a if aa < 5]

# same as above code

#l=[]
#for aa in a:
#    if aa < 5:
#        l.append(aa)
#

#print l

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
i = len(a)
while i >=0:
      i=i-1
      if (a[i]%2 == 0):
        b.append(a[i])
print b
print ("Next practice")

numbers = [5, 1, 4, 3, 2, 6, 7, 9]
print sorted(numbers)
print (numbers)
numbers.sort()
print(numbers)
my_string = ['aa', 'BB', 'zz', 'CC', 'dd', "EE"]
print sorted(my_string)
print sorted(my_string, reverse=True)
name = 'Som,Raghu'
new_string = name.split(',')
print (new_string)

