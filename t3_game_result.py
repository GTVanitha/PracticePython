
inp = int(input("Enter the number of matrix 3x3 or 4x4"))

# ========================================================================================================= #
# subroutines
initial =[]
def create_initial(inp):
    for r in range(inp):
        inner_lis = []
        for c in range(inp):
            val = "%d,%d" %(r,c)
            inner_lis.append(val)
        initial.append(inner_lis) 

# ========================================================================================================= #

def print_board(game_board):
    for g in game_board:
        print g

# ========================================================================================================= #

def player_inp(player, msg=''):
    if (msg):
        print msg

    print player, "move \n Enter the coordinates to enter a value in board(eg: 0,1) :" 
    co_ord = raw_input();
    
    co_ord_arr = co_ord.split(',')
    return co_ord_arr

# ========================================================================================================= #

# Calling 
create_initial(inp)
print_board(initial)

# ========================================================================================================= #
# getting input from user 

msg = ''
i = 0;
while i < inp*inp:
    # if they already gave inout, dec i and call input fuction 
    if (i%2 == 0):
        # player 1
            val = player_inp('player1', msg)
            i1 = int(val[0])
            j1 = int(val[1])
            if (initial[i1][j1] == 'X' or initial[i1][j1] == 'O'):
                msg = 'Invalid input. please give another input'
                continue
            else:
                initial[i1][j1] = 'X'
    else:
        #player 2
        val = player_inp('player2', msg)
        m = int(val[0])
        n = int(val[1])
        if (initial[m][n] == 'X' or initial[m][n] == 'O'):
            msg = 'Invalid input. please give another input'
            continue
        else:
            initial[m][n] = 'O'

    print_board(initial)
    i+=1

# ========================================================================================================= #

game = initial


def winner_check(which, table):
    winner = []
    
    for i in table:
        if len(set(i)) == 1:
            winner.append(i[0])
    
    if len(winner) >= 1:
        winner = set(winner)
        print "winner in %s wise check is: %s " %(which, winner)
    else:
        print "no winner in %s wise check" %(which)
        
#row wise check
winner_check('row', game)

# ========================================================================================================= #

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

# ========================================================================================================= #

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

# ========================================================================================================= #


