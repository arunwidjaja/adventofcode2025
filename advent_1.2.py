# Advent of Code 2025 - Day 1 Part 2

# Dial starts at 50
# Dial goes from 0 to 99
# The solution is the number of times the dial crosses over or lands on 0

import math

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
timesLandedOnZero = 0
timesCrossedOverZero = 0

print('Start dial at', currentNumber)
for adjustment in data:
    timesCrossedOverZeroCurrent = 0
    landedOnZero = False
    print(f'Move dial by: {adjustment}')
    currentNumber += adjustment

    # it crosses over if the unadjusted number is -1 or less, or 101 or more
    if currentNumber < 0 or currentNumber > (DIAL_RANGE + 1):
        if currentNumber < 0 and abs(currentNumber) < (DIAL_RANGE + 1):
            timesCrossedOverZeroCurrent = math.ceil(abs(currentNumber) / (DIAL_RANGE + 1))
            timesCrossedOverZero += timesCrossedOverZeroCurrent
        else:
            timesCrossedOverZeroCurrent = math.floor(abs(currentNumber) / (DIAL_RANGE + 1))
            timesCrossedOverZero += timesCrossedOverZeroCurrent
    currentNumber = currentNumber % (DIAL_RANGE + 1)
    if currentNumber == 0:
        landedOnZero = True
        timesLandedOnZero += 1
    if(timesCrossedOverZeroCurrent > 0):
        print(f'Times crossed over 0: {timesCrossedOverZeroCurrent}')
    if(landedOnZero):
        print("Dial landed on zero!")
    print(f'\nDial now at:  {currentNumber}')


print(f'Solution: {timesLandedOnZero + timesCrossedOverZero}')