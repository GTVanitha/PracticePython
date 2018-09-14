
data = {
        'a' : 0,
        'b' : 2.1,
        'c' : { 1 : 3 }
        }

data['c'] = 'som'
data['d'] = 'good'

print "Keys", data.keys()

# GIving only the keys
print sorted(data)

print data['b']
