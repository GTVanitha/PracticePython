
import pprint

str = " hello "


r_str = reversed(str)

print ''.join(r_str)

# only the fist letter of first word
print str.capitalize()

# Camel case
print str.title()


# List
arr = ['spam', 'eggs', 'lumberjack', 'knights', 'ni', [1,2,3,4]]

print arr[2]


# strip - not working properly - need to check again

print "==",str.strip(),"--"
print "==",str.lstrip(),"---"
print "==",str.rstrip(),"--"


print ','.join(str)


print str[2];

print arr[2]

print "After change:"

#str[2] = 'k'

arr[2] = 'k'

print arr[2]


list = ["1", "hello", 2, "world", "xxx", "world"]

print list[0]
print type(list[0])


print list[2]
print type(list[2])


list.insert(2, "I'm in ")

print list

list.remove("world")

print list


# using index
del list[0]

print list



