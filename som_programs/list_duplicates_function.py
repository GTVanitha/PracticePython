a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,12,13,11]
c = []
def lp():
    for i in a:
        if i not in c:
            c.append(i)
    return c

print(lp())

def set_fun():
        c = [set(a)]
        return c
print (set_fun())
        

