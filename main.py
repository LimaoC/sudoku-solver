import timeit


def is_valid(puzzle: list, guess: int, row: int, col: int) -> bool:
    """
    Determines whether inserting guess at (row, col) will yield a valid puzzle
    state.

    Parameters:
        puzzle: puzzle to check valid state
        guess: number to insert into puzzle
        row: row to insert into
        col: column to insert into

    Returns:
        (bool): True if puzzle state will be valid, False otherwise
    """
    # Checks corresponding row and column for duplicate values
    if guess in puzzle[row]:
        return False
    if any(guess == puzzle[rows][col] for rows in range(9)):
        return False

    # Gets the index of the corresponding 3x3 square. For example, (5, 2) ->
    # (1, 0), representing the 3x3 square in the 2nd row and 1st column.

    square_row, square_col = row // 3 * 3, col // 3 * 3
    square_row_end, square_col_end = square_row + 3, square_col + 3

    # Checks corresponding 3x3 square for duplicate values
    for srow in range(square_row, square_row_end):
        for scol in range(square_col, square_col_end):
            if guess == puzzle[srow][scol]:
                return False

    return True


def get_next_blank(puzzle: list) -> tuple:
    """
    Gets the next blank tile in the puzzle (from top left to bottom right).

    Parameters:
        puzzle: puzzle to grab blank tile from

    Returns:
        (tuple): tuple containing the (row, col) of the blank tile, or (-1, -1)
            if there are no more blank tiles.
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return (row, col)

    return (-1, -1)


def solve(puzzle: list) -> bool:
    """
    Solves the input sudoku using a backtracking algorithm.

    Parameters:
        puzzle: puzzle to solve

    Returns:
        (bool): True if the puzzle has been solved
    """
    row, col = get_next_blank(puzzle)

    if (row, col) == (-1, -1):  # Puzzle is filled
        return True
    else:
        for guess in range(1, 10):
            if is_valid(puzzle, guess, row, col):
                puzzle[row][col] = guess

                if solve(puzzle):  # Recursively attempts to solve sudoku
                    return True

                # If puzzle state is invalid, reset last guess
                puzzle[row][col] = 0

        return False


def print_grid(puzzle: list) -> None:
    """
    Prints the puzzle in a user-friendly format.

    Parameters:
        puzzle: puzzle to print
    """
    VERTICAL_BORDER = "|"
    HORIZONTAL_BORDER = "-"
    index = 0
    row = 0

    for num in range(11):
        if num in (3, 7):  # Add horizontal border
            print((HORIZONTAL_BORDER + " ") * 10 + HORIZONTAL_BORDER)
        else:
            for char in range(11):
                if char in (3, 7):  # Add vertical border
                    print(VERTICAL_BORDER + " ", end="")
                elif char == 10:  # Last number in row
                    print(str(puzzle[row][index]))
                else:
                    print(str(puzzle[row][index]) + " ", end="")
                    index += 1
            index = 0
            row += 1


def main():
    """Main logic of program"""
    # Valid input has all numbers from top left to bottom right in one string,
    # and either a 0 or a whitespace for the blank tiles.

    valid_input = False
    valid_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]

    while valid_input is False:
        puzzle = input("Input the sudoku: ")

        # Catches invalid inputs
        if len(puzzle) == 81:
            if all(char in valid_chars for char in puzzle):
                valid_input = True
            else:
                print("Invalid input type.")
        else:
            print("Invalid input length.")

    # Stores the puzzle in a nested list with 0s as the blank tiles
    puzzle = [puzzle[i:i+9] for i in range(0, len(puzzle), 9)]
    puzzle = [[int(i) if i != " " else 0 for i in j] for j in puzzle]

    # Prints initial sudoku and solved sudoku to user
    print("\nInput sudoku:")
    print_grid(puzzle)
    start_time = timeit.default_timer()
    solve(puzzle)
    end_time = timeit.default_timer()

    if solve(puzzle):
        print("\nSolved sudoku:")
        print_grid(puzzle)
        print(f"\nTook {round(end_time - start_time, 5)} seconds!")
    else:
        print("\nNo solution found.")


if __name__ == "__main__":
    main()
