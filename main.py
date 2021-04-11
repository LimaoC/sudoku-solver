def get_next_blank(puzzle: list) -> tuple:
    """
    Gets the next blank tile in the puzzle.

    Parameters:
        puzzle: puzzle to grab next blank tile from

    Returns:
        tuple: tuple containing (row, col) representing next blank tile, or
            (-1, -1) if puzzle contains no blank tiles (i.e. is filled)
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return (-1, -1)


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
    if guess in puzzle[row] or \
            any(guess == puzzle[rows][col] for rows in range(9)):
        return False

    # Gets the index of the corresponding 3x3 square. For example, (5, 2) ->
    # (1, 0), representing the 3x3 square in the 2nd row and 1st column.

    square_row, square_col = row // 3 * 3, col // 3 * 3

    # Checks corresponding 3x3 square for duplicate values
    for srow in range(square_row, square_row + 3):
        for scol in range(square_col, square_col + 3):
            if guess == puzzle[srow][scol]:
                return False

    return True


def solve(puzzle: list) -> str:
    """
    Solves the input sudoku using a backtracking algorithm.

    Parameters:
        puzzle: puzzle to solve

    Returns:

    """
    row, col = get_next_blank(puzzle)

    if (row, col) == (-1, -1):
        return puzzle


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
                print("Invalid input type")
        else:
            print("Invalid input length")

    # Stores the puzzle in a nested list with 0s as the blank tiles
    puzzle = [puzzle[i:i+9] for i in range(0, len(puzzle), 9)]
    puzzle = [[int(i) if i != " " else 0 for i in j] for j in puzzle]
    print(puzzle)


if __name__ == "__main__":
    main()
