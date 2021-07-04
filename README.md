# SudokuSolver
SudokuSolver uses a recursive backtracking algorithm (written in Python) to solve sudokus.

## Dependencies
There are no dependencies required outside of the Python standard library.

## Usage
To run the solver, clone the repository and run **main.py**. The input sudoku is a single 81 character long string with 0s or whitespaces in place of the blank tiles. Example inputs are shown below. Sudokus pulled from https://sudoku.com.au/.

Expert difficulty puzzle:
![Screenshot](https://github.com/LimaoC/sudokusolver/blob/main/Images/expert_solved.PNG)
Unsolvable puzzle:
![Screenshot](https://github.com/LimaoC/sudokusolver/blob/main/Images/unsolvable_puzzle.PNG)

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Roadmap
- [x] Implement main functionality (solving sudokus)
- [ ] Implement a GUI for the solver
- [ ] Add unit tests
