# Advent of Code 2025 - Day 2 Part 2

# ID ranges are separated by a dash.
# IDs are invalid if they consist of a repeating set of numbers.
# For example:
#   111 is invalid (1 repeated 3 times)
#   565656 is invalid (56 repeated 3 times)
# Find all of the invalid IDs in the input ranges and sum them.

with open('advent_2_input.txt', 'r') as file:
    data = file.read().split(',')

invalids = {}

"""
Helper function to check if a number is made up of a repeating set.
In this case, we can assume that the length of the number is even.
"""
# Trick:
# Concatenate the string with itself, then remove the first and last characters.
# If the original string is found in this new string, then it is a repeating set.
def isRepeating(num):
    doubledString = str(num) + str(num)
    truncatedString = doubledString[1:-1]
    if str(num) in truncatedString:
        return True
    return False

for curRange in data:
    start = int(curRange.split('-')[0])
    end = int(curRange.split('-')[1])
    rangeNums = range(start, end + 1)

    print(f'\nChecking range: {start} - {end}')
    for num in rangeNums:
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


