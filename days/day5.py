data = open("day5.txt").read().splitlines()


def part_one():
    maximum = 0
    for line in data:
        row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(line[-3:].replace('R', '1').replace('L', '0'), 2)
        maximum = max(maximum, row * 8 + col)
    return maximum


def part_two():
    possible = set(range(1024))
    for line in data:
        row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(line[-3:].replace('R', '1').replace('L', '0'), 2)
        possible.discard(row * 8 + col)

    for potential in possible:
        if potential - 1 not in possible and potential + 1 not in possible:
            return potential


print(part_one())
print(part_two())
