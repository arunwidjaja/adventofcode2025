# Advent of Code 2025 - Day 3

# Find the max possible combination of 2 digits on each line
#   The digits must be in the order they are listed
# Output the sum of these max combinations.

with open('advent_3_input.txt', 'r') as file:
    data = file.read().splitlines()

sum = 0

# Case 1: Find a digit higher than the first digit
#  Use this as the new first digit
# Case 2: Find a digit that is not higher than the first digit but higher than the second digit
#   Use this as the new second digit
# Case 3: Find a digit that is not higher than either digit
#   Move on

for line in data:
    index1 = 0
    index2 = 1
    digit1 = line[index1]
    digit2 = line[index2]

    while index2 < len(line):
        if digit1 == '9' and digit2 == '9':
            break
        if line[index2] > digit1 and index2 < len(line) - 1:
            index1 = index2
            index2 += 1
            digit1 = line[index1]
            digit2 = line[index2]
        elif line[index2] > digit2:
            digit2 = line[index2]
            index2 += 1
        else:
            index2 += 1
    sum += int(f'{digit1}{digit2}')
    
    print (f'Line: {line}')
    print(f'Max number is: {digit1}{digit2}')
print(f'Sum of all max combinations: {sum}')