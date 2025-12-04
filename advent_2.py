# Advent of Code 2025 - Day 2
# https://adventofcode.com/2025/day/2

# ID ranges are separated by a dash.
# For Part 1, IDs are invalid if they are a set of numbers repeated exactly once.
# For Part 2, IDs are invalid if they are a set of numbers repeated at least once.
# Find all of the invalid IDs in the input ranges and sum them.

with open('advent_2_input.txt', 'r') as file:
    data = file.read().split(',')

def isRepeatedTwice(num: int) -> bool:
    """
    Check if the number is a set of numbers repeated exactly once.

    Example:
        1212 -> True (12 repeated once)
        123123 -> True (123 repeated twice)
    """
    idx_1 = 0
    idx_2 = int(len(str(num)) / 2)
    while idx_2 < len(str(num)):
        if str(num)[idx_1] != str(num)[idx_2]:
            return False
        idx_1 += 1
        idx_2 += 1
    return True

def isRepeating(num: int) -> bool:
    """
    Checks if a number is a set of numbers repeated at least once.

    Example:
        1212 -> True (12 repeated once)
        111 -> True (1 repeated twice)    
    """
    # Trick:
    # Concatenate the string with itself, then remove the first and last characters.
    # If the original string is found in this new string, then it is a repeating set.
    
    doubledString = str(num) + str(num)
    truncatedString = doubledString[1:-1]
    if str(num) in truncatedString:
        return True
    return False

def solvePartOne(data: list[str]):
    invalids = {}
    for curRange in data:
        start = int(curRange.split('-')[0])
        end = int(curRange.split('-')[1])
        rangeNums = range(start, end + 1)

        for num in rangeNums:
            # Since invalid IDs are repeating sets, their length must be even
            if len(str(num)) % 2 != 0:
                continue
            # Check cache in case ranges are overlapping
            if num in invalids:
                invalids[num] += 1
                continue
            if isRepeatedTwice(num):
                invalids[num] = 1
    return sum(key * value for key, value in invalids.items())

def solvePartTwo(data: list[str]):
    invalids = {}
    for curRange in data:
        start = int(curRange.split('-')[0])
        end = int(curRange.split('-')[1])
        rangeNums = range(start, end + 1)

        for num in rangeNums:
            # Check cache in case ranges are overlapping
            if num in invalids:
                invalids[num] += 1
                continue
            if isRepeating(num):
                invalids[num] = 1
    return sum(key * value for key, value in invalids.items())

print (f'Solution for Part One: {solvePartOne(data)}')
print(f'Solution for Part Two: {solvePartTwo(data)}')


