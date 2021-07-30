import random


class Generator:
    """
    Generator is a class used for generating new games of sudoku.
    """
    def __init__(self) -> None:
        """
        Generates a random unique game of sudoku.
        """
        # Create empty grid and generate a full solution
        self._grid = [[0 for _ in range(9)] for _ in range(9)]
        self.generate()

    def generate(self) -> bool:
        """
        Generates a random unique game of sudoku.

        Returns:
            (bool): True if the puzzle has been generated
        """
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        row, col = self.get_next_blank()

        if (row, col) == (-1, -1):  # grid has been filled
            return True
        else:
            # Attempt to fill next blank tile with a random number
            random.shuffle(nums)

            for num in nums:
                if self.is_valid(num, row, col):
                    self._grid[row][col] = num

                    if self.generate():  # recursively tries to fill next tile
                        return True

                    # If puzzle state is invalid, reset last guess
                    self._grid[row][col] = 0

            return False

    def get_next_blank(self) -> tuple[int]:
        """
        Gets the next blank tile in the puzzle, working from top left to bottom
        right.

        Returns:
            (tuple): tuple containing the (row, col) index of the next blank
            tile, or (-1, -1) if there are no more blank tiles
        """
        for row in range(9):
            for col in range(9):
                if self._grid[row][col] == 0:
                    return (row, col)

        return (-1, -1)

    def is_valid(self, guess: int, row: int, col: int) -> bool:
        """
        Determines whether inserting guess at (row, col) will yield a valid
        puzzle state.

        Parameters:
            guess: number to check against puzzle state
            row: row to insert guess into
            col: column to insert guess into

        Returns:
            (bool): True if puzzle state is valid after insertion, False
            otherwise
        """
        grid = self._grid
        # Check row and column for duplicate values
        if (guess in grid[row] or
                any(guess == grid[rows][col] for rows in range(9))):
            return False

        # Get index of the corresponding 3x3 square. For example, (5, 2) ->
        # (1, 0), which is the 3x3 square in the 2nd row and 1st column.

        square_row = (row // 3 * 3, (row // 3 * 3) + 3)
        square_col = (col // 3 * 3, (col // 3 * 3) + 3)

        for srow in range(square_row[0], square_row[1]):
            for scol in range(square_col[0], square_col[1]):
                if guess == grid[srow][scol]:
                    return False

        return True
