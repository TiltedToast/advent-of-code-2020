import itertools

lines = [int(line[:-1]) for line in open("input.txt")]

for a, b in itertools.combinations(lines, 2):
    if a + b == 2020:
        print(f"Part 1: {a} * {b} = {a * b}")

for a, b, c in itertools.combinations(lines, 3):
    if a + b + c == 2020:
        print(f"Part 2: {a} * {b} * {c} = {a * b * c}")
