#! /usr/bin/env python

a = input("Enter Frist Number : ")


b =input("Enter Second Number : ")

c = lambda a,b: a+b
res = c(a,b)
print " Two numbers are : " , a,"and",b
print res

'''
c = a-b
print  "Add( %d + %d )= %d " %(a,b,c)

c = a*b
print  "Add( %d + %d )= %d " %(a,b,c)

c = a/b
print  "Add( %d + %d )= %d " %(a,b,c)

print  "Division (",a,"/",b,")=", a/b

print  b//a
'''
