a = raw_input("Enter a String to check if it is palidrome or not : ")
b = ''
b = ''.join(reversed(a))
print b
if b == a:
    print("%s is a palidrome") %a
else:
    print('%s is not a palidrome') %a
