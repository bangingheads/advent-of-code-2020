data = open("day8.txt").read().splitlines()


def part_one():
    acc, _ = traverse_data(0)
    return acc


def part_two():
    global data
    for i, line in enumerate(data):
        if "nop" in line:
            data[i] = data[i].replace("nop", "jmp")
            acc, j = traverse_data(0)
            if j == len(data):
                return acc
            else:
                data[i] = data[i].replace("jmp", "nop")
        elif "jmp" in line:
            data[i] = data[i].replace("jmp", "nop")
            acc, j = traverse_data(0)
            if j == len(data):
                return acc
            else:
                data[i] = data[i].replace("nop", "jmp")
    return None


def traverse_data(i):
    already_visited = set()
    acc = 0
    while i not in already_visited and i in range(len(data)):
        already_visited.add(i)
        instruction = data[i].split()[0]
        amount = data[i].split()[1]
        if instruction == "nop":
            i += 1
        elif instruction == "acc":
            i += 1
            acc += int(eval(amount))
        elif instruction == "jmp":
            i += int(eval(amount))
    return (acc, i)


print(part_one())
print(part_two())
