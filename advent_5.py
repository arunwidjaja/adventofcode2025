# Advent of Code 2024 - Day 5
# https://adventofcode.com/2025/day/5


with open('advent_5_input.txt', 'r') as file:
    data = file.read().splitlines()

# Split data into two lists based on empty line
empty_line_index = data.index('')
ranges = data[:empty_line_index]
ingredients = data[empty_line_index + 1:]

# Parse ranges as tuples of (start, end)
fresh_ranges = []
for r in ranges:
    start, end = r.split('-')
    fresh_ranges.append((int(start), int(end)))

fresh_available = {}

for ingredient in ingredients:
    ingredient_num = int(ingredient)
    for start, end in fresh_ranges:
        if start <= ingredient_num <= end:
            fresh_available[ingredient_num] = True
            break

print(len(fresh_available))





total_possible_fresh = 0

# Need to eliminate overlapping ranges
# Do this by building a list of non-overlapping ranges
# sort ranges by size, decreasing
# The first range is always added
# then for each subsequent range:
#   check if the start is inside an existing range
#       if it is, change the start to the end of that range + 1
#   check if the end is inside an existing range
#       if it is, change the end to the start of that range - 1
#   if the start is now greater than the end, discard the range
#   else, add the range to the list

sorted_ranges = sorted(fresh_ranges, key=lambda x: x[1] - x[0], reverse=True)
non_overlapping_ranges = []
for start, end in sorted_ranges:
    for existing_start, existing_end in non_overlapping_ranges:
        if existing_start <= start <= existing_end:
            start = existing_end + 1
        if existing_start <= end <= existing_end:
            end = existing_start - 1
    if start <= end:
        non_overlapping_ranges.append((start, end))
        total_possible_fresh += end - start + 1
print(total_possible_fresh)






