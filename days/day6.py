data = open("day6.txt").read().split("\n\n")


def part_one():
    total = 0
    for group in data:
        group = group.replace("\n", "")
        answers = set(list(group))
        total += len(answers)
    return total


def part_two():
    total = 0
    for group in data:
        total += len(set.intersection(*map(set, group.split())))
    return total

print(part_one())
print(part_two())
