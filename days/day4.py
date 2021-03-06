import re

data = open("day4.txt").read().split("\n\n")


def part_one():
    valid_ids = 0
    for x in data:
        valid_ids += valid(x)
    return valid_ids


def part_two():
    valid_ids = 0
    for x in data:
        if valid(x):
            valid_ids += validate(x)
    return valid_ids


def valid(inp):
    requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for requirement in requirements:
        if requirement not in inp:
            return False
    return True


def validate(inp):
    full_list = []
    for y in inp.split():
        full_list.append(y)
    for x in full_list:
        field = x.split(":")
        if field[0] == "byr":
            if validate_byr(field[1]) == False:
                return False
        elif field[0] == "iyr":
            if validate_iyr(field[1]) == False:
                return False
        elif field[0] == "eyr":
            if validate_eyr(field[1]) == False:
                return False
        elif field[0] == "hgt":
            if validate_hgt(field[1]) == False:
                return False
        elif field[0] == "hcl":
            if validate_hcl(field[1]) == False:
                return False
        elif field[0] == "ecl":
            if validate_ecl(field[1]) == False:
                return False
        elif field[0] == "pid":
            if validate_pid(field[1]) == False:
                return False
    return True


def validate_byr(inp):
    return len(inp) == 4 and int(inp) >= 1920 and int(inp) <= 2002


def validate_iyr(inp):
    return len(inp) == 4 and int(inp) >= 2010 and int(inp) <= 2020


def validate_eyr(inp):
    return len(inp) == 4 and int(inp) >= 2020 and int(inp) <= 2030


def validate_hgt(inp):
    if inp.endswith("cm"):
        num = int(inp[:-2])
        if num >= 150 and num <= 193:
            return True
    elif inp.endswith("in"):
        num = int(inp[:-2])
        if num >= 59 and num <= 76:
            return True
    return False


def validate_ecl(inp):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return inp in valid


def validate_hcl(inp):
    return bool(re.fullmatch(r'#[0-9a-f]{6}', inp))


def validate_pid(inp):
    return bool(re.fullmatch(r'[0-9]{9}', inp))


print(part_one())
print(part_two())
