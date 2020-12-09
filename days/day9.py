data = open("day9.txt").read().splitlines()
data = [int(line) for line in data]

answer = 0


def part_one(preamble=25):
    global answer
    current_preamble = list()
    for number in data:
        if len(current_preamble) < preamble:
            current_preamble.append(number)
            continue
        if len([x for x in current_preamble if number - x in current_preamble]) == 0:
            answer = number
            return answer
        current_preamble.pop(0)
        current_preamble.append(number)
    return False


def part_two():
    for i, line in enumerate(data):
        if line < answer:
            test = recursive_add(i, line)
            if test != False:
                return test


def recursive_add(starting, number):
    numbers_used = list([number])
    total = number
    while total < answer:
        next_number = data[starting + 1]
        total += next_number
        numbers_used.append(next_number)
        starting += 1
    if total == answer:
        return min(numbers_used) + max(numbers_used)
    return False


print(part_one())
print(part_two())
