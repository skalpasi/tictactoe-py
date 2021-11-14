board = [['■','■','■'],['■','■','■'],['■','■','■']]
print("TicTacToe")
for i in board:
    for j in i:
        print(j, end=" ")
    print()
print("--------------")
def isNotFilled(i,j):
    if board[c1][c2] == '✕' or board[c1][c2] == 'o':
        return False
    return True
def check():
    for i in range(3):
        c1 = board[i][0]==board[i][1]==board[i][2]=='✕'
        c2 = board[0][i]==board[1][i]==board[2][i]=='✕'
        c3 = board[0][0]==board[1][1]==board[2][2]=='✕'
        c4 = board[0][2]==board[2][2]==board[2][0]=='✕'
        c5 = board[i][0]==board[i][1]==board[i][2]=='o'
        c6 = board[0][i]==board[1][i]==board[2][i]=='o'
        c7 = board[0][0]==board[1][1]==board[2][2]=='o'
        c8 = board[0][2]==board[2][2]==board[2][0]=='o'
        if c1 or c2 or c3 or c4:
            print("player 1 win")
            exit()
        if c5 or c6 or c7 or c8:
            print("player 2 win")
            exit()
k=1
while (True):
    if k%2!=0:
        player=1
    else:
        player=2
    print("player " + str(player) + "'s turn")
    c = input()
    c1 = int(c[0])-1
    c2 = int(c[1])-1    
    if player==1 and isNotFilled(c1,c2):
        board[c1][c2] = '✕'
        k+=1
    elif player==2 and isNotFilled(c1,c2):
        board[c1][c2] = 'o'
        k+=1
    else:
        print("wrong move")
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
    check()
    print("--------------")