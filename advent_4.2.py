# Advent of Code 2024 - Day 4, Part 2

# Input is a grid
# The @ represents a roll of paper
# A roll of paper is accessible if it has fewer than four rolls of paper neighboring it
#   "Neighboring" means adjacent or diagonal (8 possible directions)
# Output the number of accessible rolls of paper

# Rolls are True, empty spaces are False
with open('advent_4_input.txt', 'r') as file:
    grid = [[char == '@' for char in line] for line in file.read().splitlines()]

"""
Gets coordinates for all accessible rolls in the grid
"""
def getAccessibleRolls(grid): 
    cols = len(grid[0])
    rows = len(grid)

    # dictionary to hold counts of neighboring rolls for each space
    rollNeighborCounts = {}

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                if (i, j) not in rollNeighborCounts:
                    rollNeighborCounts[(i, j)] = 0
                
                neighbors = [
                    (i - 1, j),      # up
                    (i + 1, j),      # down
                    (i, j - 1),      # left
                    (i, j + 1),      # right
                    (i - 1, j - 1),  # up-left
                    (i - 1, j + 1),  # up-right
                    (i + 1, j - 1),  # down-left
                    (i + 1, j + 1),  # down-right
                ]
                # Update the count for the current space's neighbors, instead of updating its own count
                # This avoids checking spaces twice.
                for ni, nj in neighbors:
                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj]:
                        rollNeighborCounts[(ni, nj)] = rollNeighborCounts.get((ni, nj), 0) + 1

    # return rolls with fewer than 4 neighbors
    accessible_rolls = (key for key, value in rollNeighborCounts.items() if value < 4)
    return accessible_rolls

"""
Removes the accessible rolls from the grid and returns the resulting grid
"""
def removeAccessibleRolls(grid):
    accessible_rolls = getAccessibleRolls(grid)
    for i, j in accessible_rolls:
        grid[i][j] = False
    return grid

"""
Execute the removal process until no accessible rolls remain
"""
def process(grid):
    rolls_removed = 0
    accessible_count = len(grid[0]) * len(grid[1]) # maximum possible initial value is every space

    while accessible_count > 0:
        accessible_rolls = getAccessibleRolls(grid)
        accessible_count = len(list(accessible_rolls))
        print(f'Found {accessible_count} accessible rolls')

        grid = removeAccessibleRolls(grid)
        rolls_removed += accessible_count
    return rolls_removed

print('Solution:', process(grid))



