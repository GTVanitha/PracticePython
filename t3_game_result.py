
mat3 = [[1, 1, 0],
        [1, 1, 0],
        [2, 2, 0]]

mat4 = [[1,2,2,3],
        [2,2,3,1],
        [3,3,3,3],
        [3,4,4,4]]
'''
0,0 0,1 0,2
1,0 1,1 1,2
2,0 2,1 2,2
'''

inp = int(input("Enter the number of matrix 3x3 or 4x4"))

game = mat3 if(inp == 3) else mat4
# (0,0) (0,1) (0,2)
print game

def winner_check(which, table):
    winner = []
    
    for i in table:
        if len(set(i)) == 1:
            winner.append(i[0])
    
    if len(winner) >= 1:
        print "winner in %s wise check is: %s " %(which, winner)
    else:
        print "no winner in %s wise check" %(which)
        
#row wise check
winner_check('row', game)

col= []
i = 0
for r in range(inp):
    inner_li = []
    for li in game:
        first_item = li[i]
        inner_li.append(first_item)
    col.append(inner_li)
    i+=1

# col wise check
winner_check('col', col)

#diagonal array

diag = []
left_dia = []
for i in range(inp):
    for j in range(inp):
        if (i == j):
            left_dia.append(game[i][j])

diag.append(left_dia)

c = -1
right_dia = []
for g in game:
    right_dia.append(g[c])
    c -=1

diag.append(right_dia)

winner_check('diagonal', diag)



'''
# To check row wise
for i in range(inp):
    print "outer:"
    for j in range(inp):
        print "inner", i, j
        # row wise
        if (game[i][j] == game[i][j+1]):
            if (game[i][j] == game[i][j+2]):
                print "winner is ", game[i][j]
                winner = 1
        print "row check done"
        i = 0
        if (winner != 1):  
            if (game[i][j] == game[i+1][j]):
                if (game[i][j] == game[i+2][j]):
                    print "winner is ", game[i][j]
                    winner = 1
        print "col check done"

        if (winner == 1):
            break
        else:
            print "No winner break"
            break


'''


