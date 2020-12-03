data = open("day3.txt").read().splitlines()


def part_one():
    y, trees = 0, 0
    line_length = len(data[0])
    for x in range(len(data)):
        trees += data[x][y % line_length] == "#"
        y += 3
    return trees


def part_two():
    trees = [0, 0, 0, 0, 0]
    lines = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    line_length = len(data[0])
    for i, (left, right) in enumerate(lines):
        y = 0
        for x in range(len(data)):
            if x % right != 0:
                continue
            trees[i] += data[x][y % line_length] == "#"
            y += left
    total = 1
    for x in trees:
        total *= x
    return total


print(part_one())
print(part_two())
