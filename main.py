import random


class Generator:
    """
    Generator is a class used for generating new games of sudoku.
    """
    def __init__(self, min_clues: int) -> None:
        """
        Generates a random unique game of sudoku.

        Parameters:
            min_clues: the number of clues to have on the board (>= 17)
        """
        # Generate a full valid grid
        self._grid = [[0 for _ in range(9)] for _ in range(9)]
        self.generate()

        clues = 81
        rounds = 3

        while rounds > 0 and clues >= min_clues:  # unique soln iff clues >= 17
            # Get the row, column, and value of the next filled tile
            row, col = self.get_random_filled()
            tile_value = self._grid[row][col]

            # Empty the filled tile and count the number of solutions that can
            # be reached in the resulting puzzle state

            self._grid[row][col] = 0
            self._count = 0
            self.count_solutions()

            # Rollback if the resulting grid doesn't have a unique soln anymore
            if self._count > 1:
                self._grid[row][col] = tile_value
                rounds -= 1
            else:
                clues -= 1

        for i in self._grid:
            print(i)

    def generate(self) -> bool:
        """
        Generates a random unique game of sudoku.

        Returns:
            (bool): True if the puzzle has been generated
        """
        nums = [i for i in range(1, 10)]

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

    def get_random_filled(self) -> tuple[int]:
        """
        Gets a randomly chosen filled tile in the puzzle.

        Returns:
            (tuple): tuple containing the (row, col) index of the random filled
            tile
        """
        while True:
            randrow = random.randint(0, 8)
            randcol = random.randint(0, 8)

            if self._grid[randrow][randcol] != 0:
                return (randrow, randcol)

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

    def count_solutions(self) -> None:
        """
        Counts the number of solutions that can be reached from the current
        puzzle state.
        """
        # Keep a copy of the current grid state to rollback to after the count
        grid_copy = self._grid.copy()
        self._count = 0

        def solve() -> bool:
            row, col = self.get_next_blank()

            if (row, col) == (-1, -1):
                self._count += 1
                return True
            else:
                for guess in range(1, 10):
                    if self.is_valid(guess, row, col):
                        self._grid[row][col] = guess

                        if solve():
                            # Check all possible solutions before finishing
                            if guess == 9:
                                return True

                        self._grid[row][col] = 0

        # Count the number of solutions and then rollback the grid state
        solve()
        self._grid = grid_copy
