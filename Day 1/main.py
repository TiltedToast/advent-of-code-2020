import itertools

temp = []

f = open("input.txt", 'r')
lines = f.readlines()

for i in range(len(lines)):
    temp.append(int(lines[i][:-1]))

for a, b, c in itertools.combinations(temp, 3):
    if a + b + c == 2020:
        print(f"{a} * {b} * {c} = {a * b * c}")
