# Advent of Code 2025 - Day 3
# https://adventofcode.com/2025/day/3

# For Part 1, find the maximum two-digit combination from each line of digits.
# For Part 2, find the maximum twelve-digit combination from each line of digits.
# In both cases, the digits must remain in their original order.
# Output the sum of these max combinations.

with open('advent_3_input.txt', 'r') as file:
    data = file.read().splitlines()

# Case 1: Find a digit higher than the first digit
#  Use this as the new first digit
# Case 2: Find a digit that is not higher than the first digit but higher than the second digit
#   Use this as the new second digit
# Case 3: Find a digit that is not higher than either digit
#   Move on



def solvePartOne(data: list[str]):
    """
    Find the maximum two-digit combination from each line of digits.
    
    Example:
        293841 -> 94
    """
    sum = 0
    for line in data:
        index_1 = 0
        index_2 = 1
        digit_1 = line[index_1]
        digit_2 = line[index_2]

        while index_2 < len(line):
            if digit_1 == '9' and digit_2 == '9':
                break
            if line[index_2] > digit_1 and index_2 < len(line) - 1:
                index_1 = index_2
                index_2 += 1
                digit_1 = line[index_1]
                digit_2 = line[index_2]
            elif line[index_2] > digit_2:
                digit_2 = line[index_2]
                index_2 += 1
            else:
                index_2 += 1
        sum += int(f'{digit_1}{digit_2}')
    return sum

def solvePartTwo(data: list[str]):
    """
    Find the maximum twelve-digit combination from each line of digits.
    
    Example:
        234234234234278 -> 434234234278
    """
    sum = 0
    MAX_LENGTH = 12
    for line in data:
        stack = []
        k = 0

        for i in range(len(line)):
            digit = line[i]
            remaining_digits = len(line) - i
            # If not enough digits to fill MAX_LENGTH, just add the digit
            if remaining_digits + len(stack) <= MAX_LENGTH:
                stack.append(digit)
                continue
            # Pop smaller digits as long as we can still fill MAX_LENGTH
            while stack and stack[-1] < digit and len(line) - i + len(stack) > MAX_LENGTH:
                stack.pop()
            stack.append(digit)

        max_num = int(''.join(stack[0:MAX_LENGTH]))

        sum += max_num
    return sum

print(f'Solution for Part One: {solvePartOne(data)}')
print(f'Solution for Part Two: {solvePartTwo(data)}')