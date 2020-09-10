__author__ = 'Pradyumn Vikram'

import pygame
import os
import time

root = os.path.dirname(__file__)

pygame.init()
n_size = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 0, 144)
BLUE = (0, 0, 255)

WIDTH = 100
HEIGHT = 100
win_size = (310, 310)
STAT_FONT = pygame.font.SysFont('comicsans', 80)
pygame.display.set_caption('Maze Solver')
win = pygame.display.set_mode(win_size)
MARGIN = 2
O = pygame.transform.scale(pygame.image.load(os.path.join(root, 'Data\\O.png')), (WIDTH, HEIGHT))
X = pygame.transform.scale(pygame.image.load(os.path.join(root, 'Data\\X.png')), (WIDTH, HEIGHT))


# function to create and return new board
def render_board():
    board = [[None for i in range(3)] for j in range(3)]
    return board


def redraw_window(screen, grid, solve):
    win.fill(BLACK)
    img = None

    for row in range(n_size):
        for col in range(n_size):
            color = WHITE
            if grid[row][col] == 'O':
                img = O
            if grid[row][col] == 'X':
                img = X
            if img is not None:
                rect = img.get_rect()
                rect.x = ((MARGIN + WIDTH) * col + MARGIN)
                rect.y = ((MARGIN + HEIGHT) * row + MARGIN)
                screen.blit(img, rect)
                img = None
            else:

                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * col + MARGIN,
                                                 (MARGIN + HEIGHT) * row + MARGIN,
                                                 WIDTH,
                                                 HEIGHT])
    pygame.display.flip()
    pygame.display.update()


# function to print the bo


# function to retrieve moves of player (X, Y)
def get_moves(board, player):
    pos = pygame.mouse.get_pos()
    y = pos[0] // (WIDTH + MARGIN)
    x = pos[1] // (HEIGHT + MARGIN)
    if 0 <= x <= 2 and 0 <= y <= 2:
        if board[x][y] is None:
            if player == 1:
                board[x][y] = 'X'
            else:
                board[x][y] = 'O'
            return True

        else:
            # if move is already done then give player another chance
            print('Invalid Move!')
            return False
            # that's right - I know RECURSION!!!!!


# check if the board is full
def is_filled(board):
    for row in board:
        for val in row:
            if val is None:
                return False
    return True


# check if any winning move has been played and return True if there is
def winner(board):
    global text
    winn = False
    # checking for diagonal wins
    if board[0][0] == board[1][1]:
        if board[1][1] == board[2][2] and board[1][1] is not None:
            if board[0][0] == 'X':
                text = 'X won!'
            else:
                text = 'O won!'
            return True
    if board[0][2] == board[1][1]:
        if board[1][1] == board[2][0] and board[1][1] is not None:
            if board[0][2] == 'X':
                text = 'X won!'
            else:
                text = 'O won!'
            return True
    # check for row wins
    for i in range(3):
        if board[i][2] == board[i][1]:
            if board[i][1] == board[i][0] and board[i][1] is not None:
                if board[i][0] == 'X':
                    text = 'X won!'
                else:
                    text = 'O won!'
                return True
    # check for column wins
    for i in range(3):
        if board[0][i] == board[1][i]:
            if board[1][i] == board[2][i] and board[1][i] is not None:
                if board[0][i] == 'X':
                    text = 'X won!'
                else:
                    text = 'O won!'
                return True
    if is_filled(board) and winn == False:
        text = 'It\'s a tie'
        return True
    # if no case returns true then return no winner found i.e. False
    return False


# combining all functions and let the magic begin!
def main():
    global text
    run = True
    # creating board
    board = render_board()
    player = 1
    # printing initial status'
    clock = pygame.time.Clock()
    val = False
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(-1)
        redraw_window(win, board, False)
        # obtaining move and updating board
        if pygame.mouse.get_pressed()[0]:
            val = get_moves(board, player)
        # updating player value (1 - X, 2 - O)

        if player == 1 and val:
            player = 2
            val = False
        if player == 2 and val:
            player = 1
            val = False

        # check if any winner found, returns True if there is a winner
        if winner(board):
            global text

            redraw_window(win, board, False)
            message = STAT_FONT.render(text, 1, (0, 255, 255))
            win.blit(message, (55, 145))
            pygame.display.update()
            time.sleep(5)
            # function prints winner so all we need to do is break
            run = False
            break


# running it all
main()
