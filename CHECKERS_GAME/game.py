from const import BLACK, COL, GREY, RED, ROW, WHITE, SQUARESIZE, PiecePOS,PiecePOSCol
from Checkersboard import PiecePOS
import pygame


def is_a_piece_selected(row1,col1,row2,col2):
    for i in range(len(PiecePOS)):
        for j in range(len(PiecePOS[i])):
            if ((i == row1) and (j == col1)):
                if (PiecePOS[i][j] == 1) or (PiecePOS[i][j] == 2):
        
                    for q in range(len(PiecePOS)):
                        for w in range(len(PiecePOS[i])):
                            if ((q == row2) and (w == col2)):
                                if (PiecePOS[q][w] == 0):
                                    return True
                else:
                    return False
    return False


def movesoutline(wind,row1,col1):

    col = PiecePOSCol[row1][col1] 

    if(PiecePOS[row1][col1] == 1):
        if (col == 1):
            try:
                if (PiecePOS[row1 + 1][col1 + 1] == 0):
                    
                    y = SQUARESIZE * (row1 + 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 + 1) + SQUARESIZE // 2 
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")
                    
                
            
            try:
                if (PiecePOS[row1 + 1][col1 - 1] == 0):
                    y = SQUARESIZE * (row1 + 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 - 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")


            try:
                if ((PiecePOS[row1 + 1][col1 + 1] == 1) or (PiecePOS[row1 + 1][col1 + 1] == 2)) and (PiecePOSCol[row1 + 1][col1 + 1] == 2):
                    if(PiecePOS[row1 + 2][col1 + 2] == 0):

                        y = SQUARESIZE * (row1 + 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 + 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 + 1][col1 - 1] == 1) or (PiecePOS[row1 + 1][col1 - 1] == 2)) and (PiecePOSCol[row1 + 1][col1 - 1] == 2):
                    if(PiecePOS[row1 + 2][col1 - 2] == 0):

                        y = SQUARESIZE * (row1 + 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 - 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")



        if (col == 2):

            try:
                if (PiecePOS[row1 - 1][col1 + 1] == 0):
                    y = SQUARESIZE * (row1 - 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 + 1) + SQUARESIZE // 2 
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if (PiecePOS[row1 - 1][col1 - 1] == 0):
                    y = SQUARESIZE * (row1 - 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 - 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")



            try:
                if ((PiecePOS[row1 - 1][col1 + 1] == 1) or (PiecePOS[row1 - 1][col1 + 1] == 2))and (PiecePOSCol[row1 - 1][col1 + 1] == 1):
                    if(PiecePOS[row1 - 2][col1 + 2] == 0):

                        y = SQUARESIZE * (row1 - 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 + 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 - 1] == 1) or (PiecePOS[row1 - 1][col1 - 1] == 2))and (PiecePOSCol[row1 - 1][col1 - 1] == 1):
                    if(PiecePOS[row1 - 2][col1 - 2] == 0):

                        y = SQUARESIZE * (row1 - 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 - 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")
                    

    if(PiecePOS[row1][col1] == 2):
        if(col == 1):


        
            try:
                if (PiecePOS[row1 + 1][col1 + 1] == 0):
                    
                    y = SQUARESIZE * (row1 + 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 + 1) + SQUARESIZE // 2 
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")
                    
                
            
            try:
                if (PiecePOS[row1 + 1][col1 - 1] == 0):
                    y = SQUARESIZE * (row1 + 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 - 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")


            try:
                if (PiecePOS[row1 - 1][col1 - 1] == 0):
                    y = SQUARESIZE * (row1 - 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 - 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")
  

            try:
                if (PiecePOS[row1 - 1][col1 + 1] == 0):
                    y = SQUARESIZE * (row1 - 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 + 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")



            try:
                if ((PiecePOS[row1 + 1][col1 + 1] == 1) or (PiecePOS[row1 + 1][col1 + 1] == 2)) and (PiecePOSCol[row1 + 1][col1 + 1] == 2):
                    if(PiecePOS[row1 + 2][col1 + 2] == 0):

                        y = SQUARESIZE * (row1 + 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 + 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 + 1][col1 - 1] == 1) or (PiecePOS[row1 + 1][col1 - 1] == 2)) and (PiecePOSCol[row1 + 1][col1 - 1] == 2):
                    if(PiecePOS[row1 + 2][col1 - 2] == 0):

                        y = SQUARESIZE * (row1 + 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 - 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 + 1] == 1) or (PiecePOS[row1 - 1][col1 + 1] == 2)) and (PiecePOSCol[row1 - 1][col1 + 1] == 2):
                    if(PiecePOS[row1 - 2][col1 + 2] == 0):

                        y = SQUARESIZE * (row1 - 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 + 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 - 1] == 1) or (PiecePOS[row1 - 1][col1 - 1] == 2)) and (PiecePOSCol[row1 - 1][col1 - 1] == 2):
                    if(PiecePOS[row1 - 2][col1 - 2] == 0):

                        y = SQUARESIZE * (row1 - 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 - 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")

        if(col == 2):

            try:
                if (PiecePOS[row1 + 1][col1 + 1] == 0):
                    
                    y = SQUARESIZE * (row1 + 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 + 1) + SQUARESIZE // 2 
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")
                    
                
            
            try:
                if (PiecePOS[row1 + 1][col1 - 1] == 0):
                    y = SQUARESIZE * (row1 + 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 - 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")


            try:
                if (PiecePOS[row1 - 1][col1 - 1] == 0):
                    y = SQUARESIZE * (row1 - 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 - 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")
  

            try:
                if (PiecePOS[row1 - 1][col1 + 1] == 0):
                    y = SQUARESIZE * (row1 - 1) + SQUARESIZE // 2
                    x = SQUARESIZE * (col1 + 1) + SQUARESIZE // 2
                    pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Bounary")



            try:
                if ((PiecePOS[row1 + 1][col1 + 1] == 1) or (PiecePOS[row1 + 1][col1 + 1] == 2)) and (PiecePOSCol[row1 + 1][col1 + 1] == 1):
                    if(PiecePOS[row1 + 2][col1 + 2] == 0):

                        y = SQUARESIZE * (row1 + 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 + 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 + 1][col1 - 1] == 1) or (PiecePOS[row1 + 1][col1 - 1] == 2)) and (PiecePOSCol[row1 + 1][col1 - 1] == 1):
                    if(PiecePOS[row1 + 2][col1 - 2] == 0):

                        y = SQUARESIZE * (row1 + 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 - 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 + 1] == 1) or (PiecePOS[row1 - 1][col1 + 1] == 2)) and (PiecePOSCol[row1 - 1][col1 + 1] == 1):
                    if(PiecePOS[row1 - 2][col1 + 2] == 0):

                        y = SQUARESIZE * (row1 - 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 + 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 - 1] == 1) or (PiecePOS[row1 - 1][col1 - 1] == 2)) and (PiecePOSCol[row1 - 1][col1 - 1] == 1):
                    if(PiecePOS[row1 - 2][col1 - 2] == 0):

                        y = SQUARESIZE * (row1 - 2) + SQUARESIZE // 2
                        x = SQUARESIZE * (col1 - 2) + SQUARESIZE // 2 
                        pygame.draw.circle(wind, GREY, ( x , y), SQUARESIZE // 2 - 40)
            except:
                print("Boundary")


def movevalid(row1,col1, row2,col2):

    col = PiecePOSCol[row1][col1]
    if(PiecePOS[row1][col1] == 1):
        if (col == 1):


            try:
                if (PiecePOS[row1 + 1][col1 + 1] == 0):
                    if(row2 == (row1 + 1) and col2 == (col1 + 1)):
                        return True
            except:
                    print("Boundary")
                
            try:
                if (PiecePOS[row1 + 1][col1 - 1] == 0):
                    if(row2 == (row1 + 1) and col2 == (col1 - 1)):
                        return True
            except:
                    print("Boundary")


            try:   
                if ((PiecePOS[row1 + 1][col1 + 1] == 1)  or (PiecePOS[row1 + 1][col1 + 1] == 2)) and (PiecePOSCol[row1 + 1][col1 + 1] == 2):
                    if(PiecePOS[row1 + 2][col1 + 2] == 0):
                        if(row2 == (row1 + 2) and col2 == (col1 + 2)):
                            PiecePOS[row1 + 1][col1 + 1] = 0
                            return True
            except:
                    print("Boundary")
                


            try:
                if ((PiecePOS[row1 + 1][col1 - 1] == 1) or (PiecePOS[row1 + 1][col1 - 1] == 2)) and (PiecePOSCol[row1 + 1][col1 - 1] == 2):
                    if(PiecePOS[row1 + 2][col1 - 2] == 0):
                        if(row2 == (row1 + 2) and col2 == (col1 - 2)):
                            PiecePOS[row1 + 1][col1 - 1] = 0
                            return True
            except:
                    print("Boundary")



        if (col == 2):

            try:   
                if (PiecePOS[row1 - 1][col1 + 1] == 0):
                    if(row2 == (row1 - 1) and col2 == (col1 + 1)):
                        return True
            except:
                print("Boundary")



            try:
                if (PiecePOS[row1 - 1][col1 - 1] == 0):
                    if(row2 == (row1 - 1) and col2 == (col1 - 1)):
                        return True
            except:
                    print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 + 1] == 1) or (PiecePOS[row1 - 1][col1 + 1] == 2)) and (PiecePOSCol[row1 - 1][col1 + 1] == 1):
                    if(PiecePOS[row1 - 2][col1 + 2] == 0):
                        if(row2 == (row1 - 2) and col2 == (col1 + 2)):
                            PiecePOS[row1 - 1][col1 + 1] = 0
                            return True
            except:
                print("Boundary")

            try:
                if ((PiecePOS[row1 - 1][col1 - 1] == 1) or (PiecePOS[row1 - 1][col1 - 1] == 2)) and (PiecePOSCol[row1 - 1][col1 - 1] == 1):
                    if(PiecePOS[row1 - 2][col1 - 2] == 0):
                        if(row2 == (row1 - 2) and col2 == (col1 - 2)):
                            PiecePOS[row1 - 1][col1 - 1] = 0
                            return True
            except:
                    print("Boundary")

        print(row1,col1, row2,col2)
        return False
                
    if(PiecePOS[row1][col1] == 2):
        if(col == 1):

            try:
                if (PiecePOS[row1 + 1][col1 + 1] == 0):
                    if(row2 == (row1 + 1) and col2 == (col1 + 1)):
                        return True
            except:
                print("Bounary")
                    
            
            try:
                if (PiecePOS[row1 + 1][col1 - 1] == 0):
                    if(row2 == (row1 + 1) and col2 == (col1 - 1)):
                        return True
            except:
                print("Bounary")


            try:
                if (PiecePOS[row1 - 1][col1 - 1] == 0):
                    if(row2 == (row1 - 1) and col2 == (col1 - 1)):
                        return True
            except:
                print("Bounary")
  

            try:
                if (PiecePOS[row1 - 1][col1 + 1] == 0):
                    if(row2 == (row1 - 1) and col2 == (col1 + 1)):
                        return True
            except:
                print("Bounary")



            try:
                if ((PiecePOS[row1 + 1][col1 + 1] == 1) or (PiecePOS[row1 + 1][col1 + 1] == 2)) and (PiecePOSCol[row1 + 1][col1 + 1] == 2):
                    if(PiecePOS[row1 + 2][col1 + 2] == 0):
                        if(row2 == (row1 + 2) and col2 == (col1 + 2)):
                            PiecePOS[row1 + 1][col1 + 1] = 0
                            return True
            except:
                    print("Boundary")
                
          


            try:
                if ((PiecePOS[row1 + 1][col1 - 1] == 1) or (PiecePOS[row1 + 1][col1 - 1] == 2)) and (PiecePOSCol[row1 + 1][col1 - 1] == 2):
                    if(PiecePOS[row1 + 2][col1 - 2] == 0):

                        if(row2 == (row1 + 2) and col2 == (col1 - 2)):
                            PiecePOS[row1 + 1][col1 - 1] = 0
                            return True
            except:
                    print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 + 1] == 1) or (PiecePOS[row1 - 1][col1 + 1] == 2)) and (PiecePOSCol[row1 - 1][col1 + 1] == 2):
                    if(PiecePOS[row1 - 2][col1 + 2] == 0):
                        if(row2 == (row1 - 2) and col2 == (col1 + 2)):
                            PiecePOS[row1 - 1][col1 + 1] = 0
                            return True
            except:
                    print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 - 1] == 1) or (PiecePOS[row1 - 1][col1 - 1] == 2)) and (PiecePOSCol[row1 - 1][col1 - 1] == 2):
                    if(PiecePOS[row1 - 2][col1 - 2] == 0):
                        if(row2 == (row1 - 2) and col2 == (col1 - 2)):
                            PiecePOS[row1 - 1][col1 - 1] = 0
                            return True   
            except:
                    print("Boundary")

        if(col == 2):

        
            try:
                if (PiecePOS[row1 + 1][col1 + 1] == 0):
                    if(row2 == (row1 + 1) and col2 == (col1 + 1)):
                        return True
            except:
                print("Bounary")
                    
                
            
            try:
                if (PiecePOS[row1 + 1][col1 - 1] == 0):
                    if(row2 == (row1 + 1) and col2 == (col1 - 1)):
                        return True
            except:
                print("Bounary")


            try:
                if (PiecePOS[row1 - 1][col1 - 1] == 0):
                    if(row2 == (row1 - 1) and col2 == (col1 - 1)):
                        return True
            except:
                print("Bounary")
  

            try:
                if (PiecePOS[row1 - 1][col1 + 1] == 0):
                    if(row2 == (row1 - 1) and col2 == (col1 + 1)):
                        return True
            except:
                print("Bounary")



            try:
                if ((PiecePOS[row1 + 1][col1 + 1] == 1) or (PiecePOS[row1 + 1][col1 + 1] == 2)) and (PiecePOSCol[row1 + 1][col1 + 1] == 1):
                    if(PiecePOS[row1 + 2][col1 + 2] == 0):
                        if(row2 == (row1 + 2) and col2 == (col1 + 2)):
                            PiecePOS[row1 + 1][col1 + 1] = 0
                            return True
            except:
                    print("Boundary")
                
          


            try:
                if ((PiecePOS[row1 + 1][col1 - 1] == 1) or (PiecePOS[row1 + 1][col1 - 1] == 2)) and (PiecePOSCol[row1 + 1][col1 - 1] == 1):
                    if(PiecePOS[row1 + 2][col1 - 2] == 0):

                        if(row2 == (row1 + 2) and col2 == (col1 - 2)):
                            PiecePOS[row1 + 1][col1 - 1] = 0
                            return True
            except:
                    print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 + 1] == 1) or (PiecePOS[row1 - 1][col1 + 1] == 2)) and (PiecePOSCol[row1 - 1][col1 + 1] == 1):
                    if(PiecePOS[row1 - 2][col1 + 2] == 0):
                        if(row2 == (row1 - 2) and col2 == (col1 + 2)):
                            PiecePOS[row1 - 1][col1 + 1] = 0
                            return True
            except:
                    print("Boundary")


            try:
                if ((PiecePOS[row1 - 1][col1 - 1] == 1) or (PiecePOS[row1 - 1][col1 - 1] == 2)) and (PiecePOSCol[row1 - 1][col1 - 1] == 1):
                    if(PiecePOS[row1 - 2][col1 - 2] == 0):
                        if(row2 == (row1 - 2) and col2 == (col1 - 2)):
                            PiecePOS[row1 - 1][col1 - 1] = 0
                            return True   
            except:
                    print("Boundary")


def make_king(row1,col1,row2,col2): 
    
    col = PiecePOSCol[row1][col1]

    if (col == 1):
        if (row2 == 7):
            PiecePOS[row1][col1] = 2
           



    
    if (col == 2):
        if (row2 == 0):
            PiecePOS[row1][col1] = 2
          

