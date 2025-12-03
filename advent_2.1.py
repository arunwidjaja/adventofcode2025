# Advent of Code 2025 - Day 2

# ID ranges are separated by a dash.
# IDs are invalid if they consist of a set of numbers repeated twice.
# For example:
#   1212 is invalid (12 repeated)
#   55 is invalid (5 repeated)
# Find all of the invalid IDs in the input ranges and sum them.

with open('advent_2_input.txt', 'r') as file:
    data = file.read().split(',')

invalids = {}

"""
Helper function to check if a number is made up of a repeating set.
In this case, we can assume that the length of the number is even.
"""
def isRepeating(num):
    idx_1 = 0
    idx_2 = int(len(str(num)) / 2)
    while idx_2 < len(str(num)):
        if str(num)[idx_1] != str(num)[idx_2]:
            return False
        idx_1 += 1
        idx_2 += 1
    return True

for curRange in data:
    start = int(curRange.split('-')[0])
    end = int(curRange.split('-')[1])
    rangeNums = range(start, end + 1)

    print(f'\nChecking range: {start} - {end}')
    for num in rangeNums:
        # Since invalid IDs are repeating sets, their length must be even
        if len(str(num)) % 2 != 0:
            continue
        # Check cache in case ranges are overlapping
        if num in invalids:
            invalids[num] += 1
            print(f'Found invalid ID: {num} (cached)')
            continue
        if isRepeating(num):
            invalids[num] = 1
            print(f'Found invalid ID: {num}')

solution = sum(key * value for key, value in invalids.items())
print('\nSolution:', solution)


