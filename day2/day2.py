safe = 0

#part1
with open("input.txt", "r") as file:
    for line in file: # for each line
        int_list = [int(x) for x in line.split()]
        if (all((x < y or x > y) and 1 <= (y - x) <= 3 for x, y in zip(int_list, int_list[1:]))):
            safe = safe + 1

print(f"Part 1: {safe}")

#part2
safe = 0
with open("input.txt", "r") as file:
    for line in file: # for each line
        int_list = [int(x) for x in line.split()]
        is_safe = False
        if (all((x < y or x > y) and 1 <= (y - x) <= 3 for x, y in zip(int_list, int_list[1:]))):
            is_safe = True

        if (is_safe == False):
            for i in range(len(int_list)):
                modified_list = int_list[:i] + int_list[i+1:]
                if (all(x < y and 1 <= (y - x) <= 3 for x, y in zip(modified_list, modified_list[1:]))):
                    is_safe = True
                if (all(x > y and 1 <= (x - y) <= 3 for x, y in zip(modified_list, modified_list[1:]))):
                    is_safe = True
        if (is_safe):
            safe = safe + 1

print(f"Part 2: {safe}")