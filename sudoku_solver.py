def display_grid(grid):
    for r in range(9):
        line = ""
        for c in range(9):
            line += str(grid[r][c]) + " "
        print(line)

def locate_zero(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None

def check_placement(grid, r, c, val):
    if val in grid[r]:
        return False
        
    for row_idx in range(9):
        if grid[row_idx][c] == val:
            return False
            
    block_r = (r // 3) * 3
    block_c = (c // 3) * 3
    
    for i in range(block_r, block_r + 3):
        for j in range(block_c, block_c + 3):
            if grid[i][j] == val:
                return False
                
    return True

def run_solver(grid):
    target = locate_zero(grid)
    
    if not target:
        return True
    
    row, col = target
    
    for digit in range(1, 10):
        if check_placement(grid, row, col, digit):
            grid[row][col] = digit
            
            if run_solver(grid):
                return True
                
            grid[row][col] = 0
            
    return False

sudoku_data = [
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

if run_solver(sudoku_data):
    print("New puzzle solved successfully:\n")
    display_grid(sudoku_data)
else:
    print("No valid solution found for this board.")
          
