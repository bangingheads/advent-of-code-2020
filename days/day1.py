data = open("day1.txt").read().splitlines()

def part_one():
    for x in data:
        for y in data:
            if int(x) + int(y) == 2020:
                return int(x)*int(y)

def part_two():
    for x in data:
        for y in data:
            for z in data:
                if int(x) + int(y) + int(z) == 2020:
                    return int(x)*int(y)*int(z)

print(part_one())
print(part_two())