__author__ = 'Pradyumn Vikram'

#function to create and return new board
def render_board():
    board = [[None for i in range(3)] for j in range(3)]
    return board

#functoin to print the board
def print_board(board):
    print('  0    1    2', end='')

    i = 0
    for row in board:
        print()
        count = 0
        print(' -------------')
        
        print(i, end = '')
        for val in row:
            count += 1
            print('| ', end='')
            if val != None:
                print(val, end=' ')
            else:
                print(' ', end=' ')

            if count == 3:
                i += 1
                print('|', end='')
                count = 0
    print()
    print(' -------------')

#function to retrieve moves of player (X, Y)
def get_moves(board, player):
    x = int(input('Give X co-ordinate: '))
    y = int(input('Give Y co-ordinate: '))
    if x >= 0 and x <= 2:
        if y >= 0 and y <= 2:
            if board[x][y] == None:
                if player == 1:
                    board[x][y] = 'X'
                else:
                    board[x][y] = 'O'
                    
            else:
                #if move is aldready done then give player another chance
                print('Invalid Move!')
                get_moves(board, player) #that's right - I know RECURSION!!!!!

#check if the board is full
def is_filled(board):
    for row in board:
        for val in row:
            if val == None:
                return False
    return True

#check if any winning move has been played and return True if there is
def winner(board):
    winner = False
    #checking for diagonal wins
    if board[0][0] == board[1][1]:
        if board[1][1] == board[2][2] and board[1][1] != None:
            if board[0][0] == 'X':
                print('X won!')
            else:
                print('O won!')
            return True
    if board[0][2] == board[1][1]:
        if board[1][1] == board[2][0] and board[1][1] != None:
            if board[0][0] == 'X':
                print('X won!')
            else:
                print('O won!')
            return True
    #check for row wins
    for i in range(3):
        if board[i][2] == board[i][1]:
            if board[i][1] == board[i][0] and board[i][1] != None:
                if board[i][0] == 'X':
                    print('X won!')
                else:
                    print('O won!')
                return True
    #check for column wins
    for i in range(3):
        if board[0][i] == board[1][i]:
            if board[1][i] == board[2][i] and board[1][i] != None:
                if board[0][i] == 'X':
                    print('X won!')
                else:
                    print('O won!')
                return True
    if is_filled(board) and winner == False:
        print('It\'s a tie!')
        return True
    #if no case returns true then return no winner found i.e. False
    return False


#combiing all functions and let the magic begin!
def main():
    run = True
    #creating board
    board = render_board()
    player = 1
    #printing initial status
    print_board(board)
    while run:
        #obtaining move and updating board
        get_moves(board, player)
        #updating player value (1 - X, 2 - O)
        if player == 1:
            player = 2
        else:
            player = 1
        #print board after every iteration, cuz we gotta know what;s haapening
        print_board(board)
        #check if any winner found, returns True if there is a winner
        if winner(board):
            #function prints winner so all we need to do is break
            run = False
            break


#running it all
main()
