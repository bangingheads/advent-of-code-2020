data = open("day10.txt").read().splitlines()
data = [int(line) for line in data]
data.sort()
data = [0] + data + [max(data) + 3]


def part_one():
    differences = {
        1: 0,
        3: 0,
    }
    for i in range(1, len(data)):
        differences[data[i] - data[i - 1]] += 1
    return differences[1] * differences[3]


arrangements = {}


def num_of_possibilities(adapters):
    if len(adapters) in arrangements:
        return arrangements[len(adapters)]
    adapter = adapters[0]
    if len(adapters) == 1:
        return 1

    total = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapter < 4:
            total += num_of_possibilities(adapters[i:])
        else:
            break
    arrangements[len(adapters)] = total
    return total


def part_two():
    return num_of_possibilities(data)


print(part_one())
print(part_two())
