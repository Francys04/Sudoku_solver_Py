# # position of x and y for number
# # chech 3x3 box
# x = 3 # 5 .... num
# y = 4 # 6 .... num

# x0 = (x // 3) * 3
# y0 = (x // 3) * 3

# print(x0)
# print(y0)

from gui_solver_sudoku import solve
def test_sudoku_solver():
    # Test case 1: Easy Sudoku
    grid1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solve(grid1)
    assert is_valid_solution(grid1), "Test case 1 failed"

    # Test case 2: Empty Sudoku
    grid2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    solve(grid2)
    assert is_valid_solution(grid2), "Test case 2 failed"

    # Test case 3: Unsolved Sudoku
    grid3 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 0]
    ]
    solve(grid3)
    assert is_valid_solution(grid3), "Test case 3 failed"


def is_valid_solution(grid):
    # Check rows and columns for duplicates
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            if grid[i][j] != 0:
                if grid[i][j] in row_set:
                    return False
                row_set.add(grid[i][j])
            if grid[j][i] != 0:
                if grid[j][i] in col_set:
                    return False
                col_set.add(grid[j][i])

    # Check each 3x3 subgrid for duplicates
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_set = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if grid[x][y] != 0:
                        if grid[x][y] in subgrid_set:
                            return False
                        subgrid_set.add(grid[x][y])

    return True

"""This is a special Python conditional statement that checks whether the script 
is being run directly or if it's being imported as a module into another script."""
if __name__ == "__main__":
    """When the script is run directly (not imported as a module), this line calls the test_sudoku_solver() function,
    which contains the test cases for your Sudoku solver. This line essentially executes the defined test cases."""
    test_sudoku_solver()
    print("All test cases passed!")