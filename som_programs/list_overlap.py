a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
i = 0
new_list = []
if len(a) < len(b):
    c = len(a)
else:
    c = len(b)

while i < c:
    if (a[i] in  b ):
        if (a[i] not in new_list):
            new_list.append(a[i])
        i = i + 1
    else :
        i = i + 1
print new_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = [a_ele for a_ele in set(a) if(a_ele in b) ];
print new_list
