data = open("day3.txt").read().splitlines()


def part_one():
    y = 0
    coordinate = 0
    trees = 0
    for x in range(len(data)):
        if data[x][coordinate] == "#":
            trees += 1
        y += 3
        coordinate = y % 31
    return trees


def part_two():
    trees = [0, 0, 0, 0, 0]
    lines = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for i, (left, right) in enumerate(lines):
        y = 0
        coordinate = 0
        for x in range(len(data)):
            if x % right != 0:
                continue
            if data[x][coordinate] == "#":
                trees[i] += 1
            y += left
            coordinate = y % 31
    total = 1
    for x in trees:
        total *= x
    return total


print(part_one())
print(part_two())
