# Logic Puzzle Solver: Cryptarithmetic

This project provides a Python-based solution for the classic "TWO + TWO = FOUR" cryptarithmetic puzzle. It uses a brute-force search approach to find a unique digit mapping for each letter that satisfies the mathematical equation.

## Overview
The script leverages the `itertools` library to test permutations of digits 0-9. It ensures that:
- Each letter represents a unique digit.
- Leading letters (T and F) do not represent zero.
- The sum of the numerical values matches the puzzle requirements.

## How to Run
Ensure you have Python 3.x installed. Run the script via terminal:
```bash
python crypt_solver.py
