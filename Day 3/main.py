lines = [list(line.strip()) for line in open("input.txt")]


def check_slope(right, down):
    trees = 0
    y = 0
    for x in range(0, len(lines), down):
        if lines[x][y] == "#":
            trees += 1
        y = (y + right) % len(lines[0])
    return trees


### Part 1

print(check_slope(3, 1))

### Part 2

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

result = 1
for slope in slopes:
    result *= check_slope(*slope)
print(result)
