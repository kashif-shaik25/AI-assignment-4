# Sudoku Backtracking Solver

This repository contains a robust Python implementation of a Sudoku solver. The engine utilizes a depth-first search (DFS) backtracking algorithm to find solutions for any valid 9x9 Sudoku puzzle.

## Technical Overview
The solver treats the Sudoku grid as a constraint satisfaction problem. It systematically fills empty cells (represented by `0`) and validates each entry against three primary constraints:
1. **Row Constraint**: Each number (1-9) must appear exactly once per row.
2. **Column Constraint**: Each number (1-9) must appear exactly once per column.
3. **Box Constraint**: Each number (1-9) must appear exactly once within each 3x3 subgrid.

## Project Structure
- `display_grid`: A utility function to print the 9x9 board in a readable format.
- `locate_zero`: A search function that identifies the next unassigned cell in the grid.
- `check_placement`: The core validation logic that enforces Sudoku rules.
- `run_solver`: The recursive engine that manages state, attempts digits, and backtracks upon encountering conflicts.

## Usage
To solve the pre-loaded puzzle, run the script from your terminal:

```bash
python sudoku_solver.py
