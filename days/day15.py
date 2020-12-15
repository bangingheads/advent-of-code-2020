data = open("day15.txt").read().replace("\n", "").split(",")
data = [int(x) for x in data]


def find_last_number(data, stop):
    previous = data[-1]
    turn = len(data)
    last_spoken = {value: key + 1 for key, value in enumerate(data[:-1])}
    while turn < stop:
        new_number = turn - \
            last_spoken[previous] if previous in last_spoken else 0
        last_spoken[previous] = turn
        previous = new_number
        turn += 1
    return previous


def part_one():
    return find_last_number(data, 2020)


def part_two():
    return find_last_number(data, 30000000)


print(part_one())
print(part_two())
