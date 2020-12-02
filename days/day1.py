import sys

data = open("day1.txt").read().splitlines()
section = 2

if section == 1:
    for x in data:
        for y in data:
            if int(x) + int(y) == 2020:
                print(x*y)
                sys.exit()

elif section == 2:
    for x in data:
        for y in data:
            for z in data:
                if int(x) + int(y) + int(z) == 2020:
                    print(x*y*z)
                    sys.exit()
