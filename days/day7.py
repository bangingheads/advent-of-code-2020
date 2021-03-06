data = open("day7.txt").read().splitlines()

bags = {}
total = set()


def part_one():
    global bags
    global total
    bags = {}
    contains_gold = []
    for line in data:
        bags.update({
            line.split("bag")[0].strip(): [x.split("bag")[0].strip()[2:] for x in line.split("contain")[1].split(",") if "no" not in x]
        })
        if "shiny gold" in line.split("contain")[1]:
            contains_gold.append(line.split("bag")[0].strip())
    get_all_bags(contains_gold)
    return len(total)


def contains(string):
    has = []
    for x in bags:
        if string in bags[x]:
            has.append(x)
    return has


def get_all_bags(check_list):
    global total
    for bag in check_list:
        total.add(bag)
        new_list = contains(bag)
        for x in new_list:
            total.add(x)
            get_all_bags(contains(x))


def part_two():
    global bags
    bags = {}
    for line in data:
        bags.update({
            line.split("bag")[0].strip(): [x.split("bag")[0].strip() for x in line.split("contain")[1].split(",") if "no" not in x]
        })
    return calculate_total(bags['shiny gold'])


def calculate_total(bag_list):
    total = 0
    for bag in bag_list:
        total += int(bag.split(" ", 1)[0])
        total += int(bag.split(" ", 1)[0]) * \
            calculate_total(bags[bag.split(" ", 1)[1]])
    return total


print(part_one())
print(part_two())
