import re
from itertools import combinations

data = open("day14.txt").read().splitlines()

memory_string = re.compile(r'mem\[(\d+)\] = (\d+)$')


def part_one():
    memory = {}
    mask_or = 0
    mask_and = -1
    for line in data:
        if line.startswith("mask"):
            mask = line.split("=")[-1].strip()
            mask_or = int(mask.replace('X', '0'), 2)
            mask_and = int(mask.replace('X', '1'), 2)
        else:
            matches = memory_string.match(line)
            target = int(matches[1])
            number = int(matches[2])
            masked = (number | mask_or) & mask_and
            memory[target] = masked
    return sum(memory.values())


def part_two():
    memory = {}
    for line in data:
        if line.startswith("mask"):
            mask = line.split("=")[-1].strip()
        else:
            matches = memory_string.match(line)
            target = int(matches[1])
            number = int(matches[2])
            target_binary = bin(target)[2:].zfill(len(mask))
            binary_string = ""
            for i, character in enumerate(list(str(target_binary))):
                if mask[i] == "X":
                    binary_string += "X"
                elif mask[i] == "1" or character == "1":
                    binary_string += "1"
                else:
                    binary_string += "0"
            x_count = binary_string.count('X')
            comb_list = []
            for x in range(x_count):
                comb_list.append(0)
                comb_list.append(1)
            comb = combinations(comb_list, x_count)
            for i in sorted(set(comb)):
                change_mask = binary_string
                for j in i:
                    change_mask = change_mask.replace("X", str(j), 1)
                mem_target = int(change_mask, 2)
                memory[mem_target] = number
    return sum(memory.values())


print(part_one())
print(part_two())
