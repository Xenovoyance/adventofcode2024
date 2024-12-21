list1 = []
list2 = []
index = 0
tot1 = 0
tot2 = 0

with open("input.txt", "r") as file:
    for line in file:
        first_item = int(line.strip().split("   ")[0])
        second_item = int(line.strip().split("   ")[1])
        list1.append(first_item)
        list2.append(second_item)

list1.sort()
list2.sort()

while index < len(list1):
    tot1 = tot1 + abs(list1[index] - list2[index])
    tot2 = tot2 + (list1[index] * int(list2.count(list1[index])))
    index += 1

print(f"Part 1: {tot1}")
print(f"Part 2: {tot2}")