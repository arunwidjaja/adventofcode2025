# Advent of Code 2024 - Day 4, Part 1

# Input is a grid
# The @ represents a roll of paper
# A roll of paper is accessible if it has fewer than four rolls of paper neighboring it
#   "Neighboring" means adjacent or diagonal (8 possible directions)
# Output the number of accessible rolls of paper

# Rolls are True, empty spaces are False
with open('advent_4_input.txt', 'r') as file:
    grid = [[char == '@' for char in line] for line in file.read().splitlines()]

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

# Count rolls with fewer than 4 neighbors
accessible_rolls = sum(1 for count in rollNeighborCounts.values() if count < 4)

print(accessible_rolls)

