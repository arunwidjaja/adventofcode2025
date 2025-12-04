# Advent of Code 2024 - Day 4, Part 2

# Input is a grid
# The @ represents a roll of paper
# A roll of paper is accessible if it has fewer than four rolls of paper neighboring it
#   "Neighboring" means adjacent or diagonal (8 possible directions)
# Output the number of accessible rolls of paper


class Grid:
    """A 2D grid where True represents a roll of paper and False represents empty space"""

    def __init__(self, data: list[list[bool]]):
        """
        Initialize the grid

        :param data: A 2D boolean array where True represents a roll
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def get(self, i: int, j: int) -> bool:
        """Get the value at position (i, j)"""
        return self.data[i][j]

    def set(self, i: int, j: int, value: bool) -> None:
        """Set the value at position (i, j)"""
        self.data[i][j] = value


# Rolls are True, empty spaces are False
with open("advent_4_input.txt", "r") as file:
    grid = Grid([[char == "@" for char in line] for line in file.read().splitlines()])


def getAccessibleRolls(grid: Grid) -> list[tuple[int, int]]:
    """
    Gets the coordinates for all accessible rolls in the grid

    :param grid: A Grid object. Rolls are TRUE.
    :return: A list of tuples representing coordinates of accessible rolls
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

    :param grid: A Grid object. Rolls are TRUE.
    :param rolls: A list of tuples representing coordinates of rolls to remove
    :return: The grid with specified rolls removed
    """
    for i, j in rolls:
        grid.set(i, j, False)
    return grid


def process(grid: Grid) -> int:
    """
    Process the grid to remove accessible rolls iteratively until none remain

    :param grid: A Grid object. Rolls are TRUE.
    :return: The total number of rolls removed
    """
    rolls_removed = 0
    accessible_count = (
        grid.cols * grid.rows
    )  # maximum possible initial value is every space

    while accessible_count > 0:
        accessible_rolls = getAccessibleRolls(grid)
        accessible_count = len(accessible_rolls)
        print(f"Found {accessible_count} accessible rolls")

        grid = removeRolls(grid, accessible_rolls)
        rolls_removed += accessible_count
    return rolls_removed


print("Solution:", process(grid))
