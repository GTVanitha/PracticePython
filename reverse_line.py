
#inp_str = raw_input("Enter a long string to reverse")
inp_str = "som is My name test is Vanitha"
str1 = inp_str.split(' ')

# a:b - range 2:3 - strating from 2 print (3-2 = 1) 
# ::b - range for alll elements in the list. b can be -1(from right to left) or +1(left to right)
# ::-2 - skip one element and print from right to left
# ::2 - skip one element and print from left to right
print ' '.join(str1[::-1])

'''
rever_str = reversed(str1)

print ' '.join(rever_str)


i = len(str1) - 1

rever_str = []

while i >= 0:
 rever_str.append(str1[i])
 i = i - 1

print ' '.join(rever_str)
'''
