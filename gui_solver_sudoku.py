# generate a example of sudoku with list of lists
import pyautogui as pag
# import numpy as nup
import time

grid = []

# create input rows from sudoku game
while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)
# if put 9 num in row than you complete the row
    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

# put time for lag , to input the num in puzzle
time.sleep(3)


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
    
    
def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])   
    
    # each number in 9 lists
    for lists in final:
        for num in lists:
            str_fin.append(str(num))
            
    
    # count how many gone by
    counter = []
    
    # use hotkey that press evry num
    # click right spot to start the read program
    for num in str_fin:
        pag.press(num)
        pag.hotkey('right')     
        counter.append(num)
        # read evrey rows and column use pyautogui whith hotkeys
        # move to down and left of 8 times for evry rows
        if len(counter)%9 == 0:
            pag.hotkey('down')
            pag.hotkey('left')
            pag.hotkey('left')
            pag.hotkey('left')
            pag.hotkey('left')
            pag.hotkey('left')
            pag.hotkey('left')
            pag.hotkey('left')
            pag.hotkey('left')
            
        
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
    Print(grid)

    
solve()