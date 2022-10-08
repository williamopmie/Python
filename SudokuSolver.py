sudokuBoard = [
    [4,0,0,  3,0,7,  6,0,0],
    [0,0,3,  0,0,2,  8,0,0],
    [0,2,8,  5,1,0,  7,0,4],

    [1,0,0,  8,2,3,  9,0,0],
    [0,0,0,  7,5,0,  1,2,8],
    [0,0,4,  0,0,9,  0,0,0],

    [6,0,2,  0,4,8,  3,5,1],
    [0,3,0,  0,7,0,  4,0,0],
    [0,0,9,  0,0,0,  2,8,0],
]

def Possible(n, y, x):
    #Check possibility for rows
    for i in range(9):
        if sudokuBoard[y][i] == n:
            return False
    
    #Check possibility for columns
    for i in range(9):
        if sudokuBoard[i][x] == n:
            return False
    
    #Find the index of the first number of box
    yBox = y - (y % 3)
    xBox = x - (x % 3)

    #Check Box
    for rNum in range(yBox, yBox + 3):
        for cNum in range(xBox, xBox + 3):
            if sudokuBoard[rNum][cNum] == n:
                return False
    
    return True

def Solve():
    for y in range(9):
        for x in range(9):
            if sudokuBoard[y][x] == 0:
                for n in range(1, 10):
                    if Possible(n, y, x):
                        sudokuBoard[y][x] = n
                        Solve()
                        sudokuBoard[y][x] = 0
                
                return False
    
    print(sudokuBoard)

print(sudokuBoard)
print(" ---------------------------")
Solve()
