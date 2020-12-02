data = open("day2.txt").read().splitlines()

def part_one():
    passwords = 0
    for x in data:
        y = x.split(" ")
        y[1] = y[1].strip(":")
        counter = y[2].count(y[1])
        number_range = y[0].split("-")
        if counter in range(int(number_range[0]), int(number_range[1]) + 1):
            passwords += 1
    return passwords

def part_two():
    passwords = 0
    for x in data:
        y = x.split(" ")
        y[1] = y[1].strip(":")
        number_range = y[0].split("-")
        first = True if y[1] == y[2][int(number_range[0])-1] else False
        second = True if y[1] == y[2][int(number_range[1])-1] else False
        if first ^ second:
            passwords += 1
    return passwords

print(part_one())
print(part_two())