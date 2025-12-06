with open('advent_6_input.txt', 'r') as file:
    data = [line.split() for line in file.read().splitlines()]

# Get the length of the lines; they are all the same length
#   call this n
# Call the number of lines k
# Loop through n.
# In each iteration, the nth character of the last line tells you to sum or product
# The the nth character of the first k-1 lines are the values to sum or product
# calculate and add to the total

total = 0
k = len(data)
n = len(data[0])

for i in range(n):
    operation = data[k-1][i]
    values = [int(data[j][i]) for j in range(k-1)]
    
    if operation == '+':
        total += sum(values)
    elif operation == '*':
        product = 1
        for value in values:
            product *= value
        total += product





# Part 2:
# This time, need to store the values as a matrix.
# Iterate through the last line first to get the operations and their indices
# The index of the operation is the starting index of the values in the previous lines
# The index of the next operation - 2 is the ending index of the values in the previous lines
#   The -2 is because there is a space between operations
# For each operation, store the values as a matrix:
#   The number of rows is 4 (fixed input). The number of columns is the ending index - starting index + 1.
#   for each of the lines before the last line, iterate from the starting index to the ending index
#   store each character in the matrix at the corresponding row and column.
# Then transpose the matrix.
# Then perform the operation, using each row as the values to sum or product.

# Read the raw file to work with individual characters
with open('advent_6_input.txt', 'r') as file:
    lines = file.read().splitlines()

