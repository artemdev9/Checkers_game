import pygame
from pygame import mouse
from const import GREY, WHITE, WIDTH, HEIGHT, SQUARESIZE, PiecePOS
from Checkersboard import set_up_board, draw_pieces, get_rowcol, move_pieces

FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHEKERS')

set_up_board(WINDOW)
draw_pieces(WINDOW)

row1 = None
col1 = None
row2 = None
col2 = None
firstclick = True


def main():
    run = True
    clock = pygame.time.Clock()
   

    while run == True:
        clock.tick(FPS)
        pygame.display.update()
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePOS = pygame.mouse.get_pos() 
                get_rowcol_for_move() 
                move_pieces(WINDOW,row1,col1,row2,col2)           


def get_rowcol_for_move():

    global firstclick, row1, col1, row2, col2

    if (firstclick == True):
    
        firstclick = False
        mousePOS = pygame.mouse.get_pos()
        row1,col1 = get_rowcol(mousePOS)
    
    elif(firstclick == False):

        
        firstclick = True
        mousePOS = pygame.mouse.get_pos()
        row2,col2 = get_rowcol(mousePOS)


def refresh():
    global row1,col1,row2,col2
    row1 = None
    col1 = None
    row2 = None
    col2 = None


main()