# Sudoku_solver

- You need to install numpy which use for a matrix is a specialized 2-D array that retains its 2-D nature through operations. It has certain special operators, such as * (matrix multiplication) and ** (matrix power).
- And pyautogui which can use  used to click, drag, scroll, move, etc. It can be used to click at an exact position.

## This application has two methods of solving this game: 
- The first would be reading the numbers from the lists in another list and displaying the final result in another list in the terminal. 
- The second version uses the pyautogui library that allows us to do different actions on a website (scroll, drag, click, etc), with the help of this library we read each line from the box after which the algorithm solved this game.



### The gui_solver_sudoku control is carried out in the following steps: 
- after we run the program, it will ask us what the numbers are in each row (the number 0 being the empty square) then it will give us an answer of 'Complete' if we enter all 9 numbers in a row ; 
- after entering each row in the terminal, we will click on the first square in the upper right corner; 
- the program with the help of the hotkey method will read each row from right to left until the last square, after which it will go to the bottom row and perform the same action; 
- the same principle was used to solve this game of entering numbers into the squares;
- finally we will see the animation when each number is entered in the empty square. 


- The site of the game is: https://sudoku.com/