a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''
new_list = [];
for a_ele in a:
    if ((a_ele in b) and (a_ele not in new_list)):
           new_list.append(a_ele)
'''
new_list = [a_ele for a_ele in set(a) if (a_ele in b)]

print new_list


w = [1,2,2,3,3,4,4,5,9,5]
# create unique unordered immutable list 
w1 = set(w)

print w

