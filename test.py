a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
i = len(a)
while i >=0:
    i=i-1
    if (a[i]%2 == 0):
        b.append(a[i])
        print b


