import numpy as np

Board = np.array([[4,0,1,2,9,0,0,7,5],
                  [2,0,0,3,0,0,8,0,0],
                  [0,7,0,0,8,0,0,0,6],
                  [0,0,0,1,0,3,0,6,2],
                  [1,0,5,0,0,0,4,0,3],
                  [7,3,0,6,0,8,0,0,0],
                  [6,0,0,0,2,0,0,3,0],
                  [0,0,7,0,0,1,0,0,4],
                  [8,9,0,0,6,5,1,0,7]])

def valid(bo, num, pos):
    y,x = pos[0],pos[1]

    ##checking in row
    for i in range(0,len(bo[y])):
        if bo[y][i] == num and i != x:
            return False

    ##checking in column
    for i in range(0, len(bo)):
        if bo[i][x] == num and i != y:
            return False

    ##checking in box
    Y = y//3
    X = x//3
    for i in range(3*Y,3*Y+3):
        for j in range(3*X,3*X+3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def Print_Board(Board):
    for i in range(len(Board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(Board[i])):
            if j % 3 ==0 and j != 0:
                print(" | ",end="")

            if j == 8:
                print(Board[i][j])
            else:
                print(str(Board[i][j]) + " ",end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i,j)
    return None

def Solve(bo):                  #this function will "FINALLY" output "TRUE" for the only correct combination of the sudoku
    pos = find_empty(bo)
    if bool(pos):               #this if indicates that there are still empty cells in our grid
        row,col = pos
    else:                       #this else will indicate that there are no empty cells left to be filled (our grid is complete !!!)
        print("\n\nSolution: \t")
        Print_Board(bo)
        return True

    for a in range(1, 10):      #loop to put all num from 1-9 in the cells
        if valid(bo,a,(row,col)):
            bo[row][col] = a

            if Solve(bo):         ##this Solve() is the solve function operated on the next empty cell.
                return True     # so this basically checks if any no. will fit in the next empty box, wherein our current cell is filled with "a"

            bo[row][col] = 0    #changing the current cell back to zero cuz Solve returned False for all 'a' in the next cell



    return False                #if the "FOR" loop was unable to fill the cell (i.e. no correct values left for the "current" cell) this will return False

Print_Board(Board)
Solve(Board)