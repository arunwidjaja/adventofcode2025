# Advent of Code 2025 - Day 4
# https://adventofcode.com/2025/day/4

# Input is a grid of '.' and '@'
# The @ represents a roll of paper
# A roll of paper is accessible if it has fewer than four rolls of paper neighboring it
#   "Neighboring" means adjacent or diagonal (8 possible directions)
# For Part 1, find the number of accessible rolls of paper
# For Part 2, remove rolls of paper until no more can be removed
#   Then, find the number of rolls removed


class Grid:
    """
    A 2D grid where True represents a roll of paper and False represents empty space
    """

    def __init__(self, data: list[list[bool]]):
        """
        Initialize the grid
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def get(self, i: int, j: int) -> bool:
        """
        Get the value at position (i, j)
        """
        return self.data[i][j]

    def set(self, i: int, j: int, value: bool) -> None:
        """
        Set the value at position (i, j)
        """
        self.data[i][j] = value


with open("advent_4_input.txt", "r") as file:
    grid = Grid([[char == "@" for char in line] for line in file.read().splitlines()])


def getAccessibleRolls(grid: Grid) -> list[tuple[int, int]]:
    """
    Gets the coordinates for all accessible rolls in the grid
    A roll is accessible if it has fewer than 4 neighboring (adjacent or diagonal) rolls.
    """
    cols = grid.cols
    rows = grid.rows

    # dictionary to hold counts of neighboring rolls for each space
    rollNeighborCounts = {}

    for i in range(rows):
        for j in range(cols):
            if grid.get(i, j):
                if (i, j) not in rollNeighborCounts:
                    rollNeighborCounts[(i, j)] = 0

                neighbors = [
                    (i - 1, j),  # up
                    (i + 1, j),  # down
                    (i, j - 1),  # left
                    (i, j + 1),  # right
                    (i - 1, j - 1),  # up-left
                    (i - 1, j + 1),  # up-right
                    (i + 1, j - 1),  # down-left
                    (i + 1, j + 1),  # down-right
                ]
                # Update the count for the current space's neighbors, instead of updating its own count
                # This avoids checking spaces twice.
                for ni, nj in neighbors:
                    if 0 <= ni < rows and 0 <= nj < cols and grid.get(ni, nj):
                        rollNeighborCounts[(ni, nj)] = (
                            rollNeighborCounts.get((ni, nj), 0) + 1
                        )

    # return rolls with fewer than 4 neighbors
    accessible_rolls = [key for key, value in rollNeighborCounts.items() if value < 4]
    return accessible_rolls


def removeRolls(grid: Grid, rolls: list[tuple[int, int]]) -> Grid:
    """
    Removes the rolls from the grid and returns the resulting grid
    """
    for i, j in rolls:
        grid.set(i, j, False)
    return grid


def solvePartOne(grid: Grid) -> int:
    """
    Finds number of rolls that can be removed in one pass
    """
    accessible_rolls = getAccessibleRolls(grid)
    return len(accessible_rolls)


def solvePartTwo(grid: Grid) -> int:
    """
    Process the grid to remove accessible rolls iteratively until none remain
    """
    num_rolls_removed = 0
    accessible_count = (
        grid.cols * grid.rows
    )  # maximum possible initial value is the total number of spaces

    while accessible_count > 0:
        accessible_rolls = getAccessibleRolls(grid)
        accessible_count = len(accessible_rolls)

        grid = removeRolls(grid, accessible_rolls)
        num_rolls_removed += accessible_count
    return num_rolls_removed


print(f"Solution for Part One: {solvePartOne(grid)}")
print(f"Solution for Part Two: {solvePartTwo(grid)}")
