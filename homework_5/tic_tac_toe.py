# Tic-tac-toe տախտակը կարող է ներկայացվել որպես 3×3 երկչափ ցուցակ,
# որտեղ զրոները նշանակում են դատարկ բջիջներ, մեկը՝ X, իսկ երկուսը
# նշանակում են O: Իրականացնել այդ խաղը օգտագործելով Python List։

print('Welcome to the best game in the world\n       TIC_TAC_TOE\n')
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
print('Please, enter player names')
player1 = input('player―1 :  ')
player2 = input('player_2 :  ')

def play():    
    res = False
    while res == False:
        if res == False:
            res = start(1)
        if res == False:
            res = start(2)
        if res == player1 or res == player2:
            print('congratulations!!!!!')
            print('The winner is ' + res.upper())
            break
    print('would you like to play again?(y/n)\n')
    while True:
        answer = input()
        if answer.lower() == 'y':
            for i in board:
                for j in i:
                    i[j] = 0
            play()
        elif answer.lower() == 'n':
            print('BYE!!!!!')
            exit()
        else:
            print("your input is not valid, input 'y' or 'n'")

def checking(player, board):
    for i in board:
        if (i[0] == i[1] and
            i[0] == i[2] and
            i[0] != 0):
            return player
    for i in range(3):
        if (board[0][i] == board[1][i] and
            board[0][i] == board[2][i] and
            board[0][i] != 0):
            return player
    if (((board[0][0] == board[1][1] and
        board[1][1] == board[2][2]) or
        (board[1][1] == board[0][2] and
        board[1][1] == board[2][0])) and
        board[1][1] != 0):
        return player
    return False

def choose_cell(player):
    print(player + ', your turn, please, choose the cell')
    while True:
        try:
            row = int(input('row :     '))
            if not row in (1, 2, 3):
                print("your input for row is not valid, please, input '1', '2' or '3'")
            else:
                break
        except:
            print("your input for row is not valid, please, input '1', '2' or '3'")
    while True:
        try:
            col = int(input('column :  '))
            if int(col) not in (1, 2, 3):
                print("your input for column is not valid, please, input '1', '2' or '3'")
            else:
                break
        except:
            print("your input for row is not valid, please, input '1', '2' or '3'")

    if board[row - 1][col - 1] != 0:
        print('that cell is already corrupted, please, choose another cell')
        choose_cell(player)
    else:
        if player == player1:   
            board[row - 1][col - 1] = 1
        elif player == player2:
            board[row - 1][col - 1] = 2
    winner = checking(player, board)
    return winner
    


def start(turn):   
    for i in board:
        print(i)
    if turn == 1:
        res = choose_cell(player1)
    else:
        res = choose_cell(player2)
    return res

play()