# Advent of Code 2025 - Day 1

# Dial starts at 50
# Dial goes from 0 to 99
# The solution is the number of times the dial lands on 0 after an adjustment

STARTING_POSITION = 50
DIAL_RANGE = 99

with open('advent_1_input.txt', 'r') as file:
    data = file.read().splitlines()
for i in range(len(data)):
    if data[i].startswith('R'):
        data[i] = int(data[i][1:])
    elif data[i].startswith('L'):
        data[i] = int('-' + data[i][1:])

currentNumber = STARTING_POSITION
timesZero = 0

print('Start dial at', currentNumber)
for adjustment in data:
    print(f'Move dial by: {adjustment:>4}')
    currentNumber += adjustment
    currentNumber = currentNumber % (DIAL_RANGE + 1)
    print(f'Dial now at:  {currentNumber:>4}\n')
    if currentNumber == 0:
        timesZero += 1

print('Solution:', timesZero)