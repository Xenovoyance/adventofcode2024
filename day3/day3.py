import re
from functools import reduce

sum = 0

# part 1 ----------------------------------
with open("input.txt", "r") as file:
    for line in file:

        # regexp for what we are looking for
        pattern = r"mul\((-?\d+),(-?\d+)\)"
        matches = re.findall(pattern, line)
        int_matches = [(int(x), int(y)) for x, y in matches]
        
        for pair in int_matches:
            # calculate using lambda
            sum = sum + reduce(lambda x, y: x * y, pair)

print(f"Part 1: {sum}")

# part 2 ----------------------------------
sum = 0
good_integers = []
full_string = ""

with open("input.txt", "r") as file:
    for line in file:
        full_string = full_string + line

# Split the string into chunks based on "do()" and "don't()"
chunks = re.split(r"(do\(\)|don't\(\))", full_string)

# Initialize variables
is_good = True  # Assume the string starts in a "good" state

# Iterate over the chunks
for i in range(0, len(chunks), 2):  # Process the markers and content
    marker = chunks[i - 1] if i > 0 else "do()"  # Default to "do()" at the start
    content = chunks[i]

    if marker == "do()":
        is_good = True
    elif marker == "don't()":
        is_good = False

    if is_good:
        # Find all `mul(x,y)` substrings in the current chunk 
        matches = re.findall(r"mul\((-?\d+),(-?\d+)\)", content)
        # Convert matches to integers and store them
        good_integers.extend((int(x), int(y)) for x, y in matches)

# Output the results

for pair in good_integers:
    # calculate using lambda
    sum = sum + reduce(lambda x, y: x * y, pair)

print(f"Part 2: {sum}")