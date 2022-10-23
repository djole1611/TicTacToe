import pygame
import sys
import numpy as np
pygame.init() #Starting 
WIDTH=400
HEIGHT=WIDTH
SCREEN_COLOR=(28,170,156)

LINE_COLOR=(23,145,135)
LINE_WIDTH=int(WIDTH/40)

BOARD_ROWS=3
BOARD_COLUMS=3

CIRCLE_RADIUS=int(HEIGHT/10)
CIRCLE_WIDTH=int(WIDTH/40)
CIRCLE_COLOR=(239,231,200)

CROSS_WIDTH=int(HEIGHT/24)
SPACE=int(WIDTH/15)
CROSS_COLOR=(66,66,66)

LINE=int(WIDTH/40)

player=1
gameover=False
#Start a display
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(SCREEN_COLOR)

board=np.zeros((BOARD_ROWS,BOARD_COLUMS))
#Check if something is in square on board
def available_square(row,column):
    if board[row][column]==0:
        return True
    else:
        return False
#Pick a square on board
def marked_square(row,column,player):
    board[row][column]=player
#End game if a board is full
def board_full():
    for row in range(BOARD_ROWS):
        for columns in range(BOARD_COLUMS):
            if board[row][columns]==0:
                return False
    return True

#Background
def draw_lines():
    pygame.draw.line(screen,LINE_COLOR,(0,WIDTH/3),(HEIGHT,WIDTH/3),LINE)
    pygame.draw.line(screen,LINE_COLOR,(0,2*WIDTH/3),(HEIGHT,2*WIDTH/3),LINE)

    pygame.draw.line(screen,LINE_COLOR,(HEIGHT/3,0),(HEIGHT/3,WIDTH),LINE)
    pygame.draw.line(screen,LINE_COLOR,(2*HEIGHT/3,0),(2*HEIGHT/3,WIDTH),LINE)
    
draw_lines()

def draw_fig():
    for row in range(BOARD_ROWS):
        for column  in range(BOARD_COLUMS):
            if board[row][column]==1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(column*HEIGHT/3+HEIGHT/6),int(row*HEIGHT/3+HEIGHT/6)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][column]==2:
                pygame.draw.line(screen,CROSS_COLOR,(column*WIDTH/3 +SPACE,row*WIDTH/3+WIDTH/3-SPACE),(column*WIDTH/3+WIDTH/3-SPACE,row*WIDTH/3+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(column*WIDTH/3+SPACE,row*WIDTH/3+SPACE),(column*WIDTH/3+WIDTH/3-SPACE,row*WIDTH/3+WIDTH/3-SPACE),CROSS_WIDTH)
def check_win(player):
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            draw_horisontal(row,player)
            return True
    for column in range(BOARD_COLUMS):
        if board[0][column]==player and board[1][column]==player and board[2][column]==player:
            draw_vertical(column,player)
            return True
        if board[0][0]==player and board[1][1]==player and board[2][2]==player:
            draw_diagonal(player)
            return True
        if board[0][2]==player and board[1][1]==player and board[2][0]==player:
            draw_diagonal2(player)
            return True
    return False
def draw_vertical(column,player):
    posX=column*WIDTH/3+WIDTH/6
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),LINE)

def draw_horisontal(row,player):
    posY=row*HEIGHT/3+HEIGHT/6
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,  posY),(WIDTH-15,posY),LINE)

def draw_diagonal(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),LINE)
def draw_diagonal2(player):
    if player==1:
        color=CIRCLE_COLOR
    elif player==2:
        color=CROSS_COLOR
    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),LINE)
def restart():
    screen.fill(SCREEN_COLOR)
    draw_lines()
    for row in range (BOARD_ROWS):
        for columns in range(BOARD_COLUMS):
            board[row][columns]=0   
    board_full
    
#mainloop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not gameover:
            mouseX= event.pos[0] #x
            mouseY= event.pos[1] #y

            clicked_row=int(mouseY  // (WIDTH/3))
            clicked_column=int(mouseX //  (HEIGHT/3))
            print(clicked_row)
            print(clicked_column)

            if available_square(clicked_row,clicked_column):
                if player==1:
                    marked_square(clicked_row,clicked_column,1)
                    if check_win(player):
                        gameover=True
                    player=2
                elif player==2:
                    marked_square(clicked_row,clicked_column,2)
                    if check_win(player):
                        gameover=True
                    player=1

                draw_fig()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()
                player=1
                gameover=False
        print()
    pygame.display.update()
