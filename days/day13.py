from functools import reduce

data = open("day13.txt").read().splitlines()


def part_one():
    start = int(data[0])
    buses = [int(x) for x in data[1].split(",") if x != "x"]
    remainders = {}
    for x in buses:
        remainders[x] = (int(start/x)*x) + x
    x, y = sorted(remainders.items(), key=lambda item: item[1])[0]
    return x * (y - start)


def part_two():
    buses = [(int(b), i) for i, b in enumerate(data[1].split(",")) if b != "x"]
    jump = i = buses[0][0]
    for b in buses[1:]:
        while (i+b[1]) % b[0] != 0:
            i += jump
        jump *= b[0]
    return i


print(part_one())
print(part_two())
