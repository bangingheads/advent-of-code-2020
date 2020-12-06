data = open("day6.txt").read().split("\n\n")


def part_one():
    total = 0
    for group in data:
        total += len(set(list(group.replace("\n", ""))))
    return total


def part_two():
    total = 0
    for group in data:
        total += len(set.intersection(*map(set, group.split())))
    return total


print(part_one())
print(part_two())
