import numpy as nup


grid = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0]
]


# x - rows & y - columns & n - 0 or empty spot
# check the number 
def possible(x, y, n):
    for i in range(0, 9):
        # Checks for number (n) in X columns
        if grid[i][x] == n and i != y: 
            return False

    for i in range(0, 9):
        # Checks for number (n) in X columns
        if grid[y][i] == n and i != x: 
            return False
# Checks for numbers in box(no matter the position, it finds the corner)
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  
            if grid[Y][X] == n:
                return False    
    return True
    
        
# backtracking
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            # if num of num = 0 we figure out what it is " 0 0 0 5" program recognize where is 0
            if grid[y][x] == 0:
                for num in range(1, 10):
                    if possible(x, y, num):
                        grid[y][x] = num
                        solve()
                        grid[y][x] = 0
                return
    print(nup.matrix(grid))
    input("More?")
    
solve()