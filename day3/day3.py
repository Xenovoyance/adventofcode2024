import re
from functools import reduce

sum = 0

with open("input.txt", "r") as file:
    for line in file: # for each line
        pattern = r"mul\((-?\d+),(-?\d+)\)"
        matches = re.findall(pattern, line)
        int_matches = [(int(x), int(y)) for x, y in matches]
        
        for pair in int_matches:
            sum = sum + reduce(lambda x, y: x * y, pair)

    print(f"Part 1: {sum}")

    