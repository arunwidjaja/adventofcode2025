# Advent of Code 2025 - Day 3

# Each line has a number.
# By removing digits, find the maximum possible 12-digit number,
#   while maintaining the order of the remaining digits.
# Output the sum of these max combinations.

with open('advent_3_input.txt', 'r') as file:
    data = file.read().splitlines()

sum = 0
MAX_LENGTH = 12

for line in data:
    stack = []
    k = 0

    for i in range(len(line)):
        digit = line[i]
        remainingDigits = len(line) - i
        # If not enough digits to fill MAX_LENGTH, just add the digit
        if remainingDigits + len(stack) <= MAX_LENGTH:
            stack.append(digit)
            continue
        # Pop smaller digits as long as we can still fill MAX_LENGTH
        while stack and stack[-1] < digit and len(line) - i + len(stack) > MAX_LENGTH:
            stack.pop()
        stack.append(digit)

    maxNum = int(''.join(stack[0:MAX_LENGTH]))

    sum += maxNum
    
    print (f'Line: {line}')
    print(f'Max number is: {maxNum}')
print(f'Sum of all max combinations: {sum}')