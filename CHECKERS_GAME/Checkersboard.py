import pygame
from const import BLACK, COL, GREY, RED, ROW, WHITE, SQUARESIZE, YELLOW, PiecePOS,PiecePOSCol
from game import is_a_piece_selected, movesoutline, movevalid, make_king


def get_rowcol(mousePOS):
    x, y = mousePOS
    row = y // SQUARESIZE
    col = x // SQUARESIZE
    return row, col


def set_up_board(wind):
    wind.fill(BLACK)
    pygame.display.flip()
          

    for row in range(ROW):
        for col in range(row % 2, COL, 2):
            pygame.draw.rect(wind, WHITE, (row*SQUARESIZE, col *SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.display.flip()
    

def draw_pieces(wind):
    for i in range(len(PiecePOS)):
        for j in range(len(PiecePOS[i])):
            if (PiecePOS[j][i] == 1):
                x = SQUARESIZE * i + SQUARESIZE // 2
                y = SQUARESIZE * j + SQUARESIZE // 2
                if (PiecePOSCol[j][i] == 1):
                    pygame.draw.circle(wind, RED, ( x , y), SQUARESIZE // 2 - 10)
                elif (PiecePOSCol[j][i] == 2):
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 10)  
                pygame.display.flip()
            if (PiecePOS[j][i] == 2):
                x = SQUARESIZE * i + SQUARESIZE // 2
                y = SQUARESIZE * j + SQUARESIZE // 2
                if (PiecePOSCol[j][i] == 1):
                    pygame.draw.circle(wind, RED, ( x , y), SQUARESIZE // 2 - 10)
                    pygame.draw.circle(wind, YELLOW, ( x , y), (SQUARESIZE // 2 - 10) - 25)
                elif (PiecePOSCol[j][i] == 2):
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 10)  
                    pygame.draw.circle(wind, YELLOW, ( x , y), (SQUARESIZE // 2 - 10) - 25)
                pygame.display.flip()
        

def move_pieces(wind, row1, col1,row2,col2):

    movesoutline(wind, row1, col1)

    if (is_a_piece_selected(row1,col1,row2,col2) == True):


        if(movevalid(row1, col1,row2,col2) == True):
            
            make_king(row1, col1,row2,col2)

            for i in range(len(PiecePOS)):
                for j in range(len(PiecePOS[i])):
                    if ((i == row1) and (j == col1)):
                        if (PiecePOS[i][j] == 1) or (PiecePOS[i][j] == 2):
                            figure = PiecePOS[i][j]
                            PiecePOS[i][j] = 0
                            col = PiecePOSCol[i][j]
                            PiecePOSCol[i][j] = 0
                        
                            
            for q in range(len(PiecePOS)):
                for w in range(len(PiecePOS[q])):
                    if ((q == row2) and (w == col2)):
                        if (PiecePOS[q][w] == 0):
                            PiecePOS[q][w] = figure
                            PiecePOSCol[q][w] = col
                        

                        set_up_board(wind)
                        draw_pieces(wind)
                        
                
            return True
        else:
            set_up_board(wind)
            draw_pieces(wind)
            
    else:
        return False
        


    

    