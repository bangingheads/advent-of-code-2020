from collections import Counter
import sys

data = open("day16.txt").read().split("\n\n")


def part_one():
    rules = data[0].split("\n")
    rules_set = set()
    for x in rules:
        for y in x.split(":")[-1].strip().split(" or "):
            i, j = y.split("-")
            for number in range(int(i), int(j) + 1):
                rules_set.add(number)
    nearby = data[2].replace(
        "nearby tickets:", "").replace("\n", ",").split(",")
    nearby = [x for x in nearby if x != '']
    total = 0
    for i, x in enumerate(nearby):
        if x != '' and int(x) not in rules_set:
            total += int(x)
    return total


def part_two():
    rules = data[0].split("\n")
    rules_dict = {}
    for x in rules:
        rules_dict[x.split(":")[0].strip()] = set()
        for y in x.split(":")[-1].strip().split(" or "):
            i, j = y.split("-")
            for number in range(int(i), int(j) + 1):
                rules_dict[x.split(":")[0].strip()].add(number)

    nearby = data[2].replace("nearby tickets:", "").split("\n")
    nearby = [x for x in nearby if x != '']
    toss_out = []
    for i, x in enumerate(nearby):
        for y in x.split(","):
            valid = False
            for z in rules_dict:
                if int(y) in rules_dict[z]:
                    valid = True
            if valid == False:
                toss_out.append(i)
                break
    rules_test = {key: list() for _, key in enumerate(rules_dict)}
    for i, x in enumerate(nearby):
        if i in toss_out:
            continue
        for j, y in enumerate(x.split(",")):
            for z in rules_dict:
                if int(y) in rules_dict[z]:
                    rules_test[z].append(j)
        if i != 0:
            for z in rules_test:
                d = Counter(rules_test[z])
                rules_test[z] = [k for k, v in d.items() if v > 1]
    rules_keys = {}
    while len(rules_test) > 0:
        for z in rules_test:
            if len(rules_test[z]) == 1:
                rules_keys[z] = rules_test[z][0]
                for y in rules_test:
                    if rules_test[z][0] in rules_test[y] and y != z:
                        rules_test[y].remove(rules_test[z][0])
                del rules_test[z]
                break
    total = 1
    my_ticket = data[1].replace("your ticket:\n", "").split(",")
    for x in rules_keys:
        if "departure" in x:
            total *= int(my_ticket[rules_keys[x]])
    return total


print(part_one())
print(part_two())
