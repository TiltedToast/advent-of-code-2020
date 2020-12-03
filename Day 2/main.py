file = open("input.txt", "r")
lines = file.readlines()
file.close()


def part_1():
    total = 0
    for i in range(len(lines)):
        min_count = int(lines[i].split("-")[0])
        max_count = int(lines[i].split()[0].split("-")[1])
        character = lines[i].split(":")[0][-1]
        password = lines[i].split()[-1]

        if min_count <= password.count(character) <= max_count:
            total += 1

    print(total)


def part_2():
    total = 0
    for i in range(len(lines)):
        first_index = int(lines[i].split("-")[0]) - 1
        second_index = int(lines[i].split()[0].split("-")[1]) - 1
        character = lines[i].split(":")[0][-1]
        password = lines[i].split()[-1]

        if password[first_index] == character or password[second_index] == character:
            if not (password[first_index] == character and password[second_index] == character):
                total += 1

    print(total)


part_1()
part_2()


class Line:
    def __init__(self, raw):
        self.raw = raw
        self.low = 0
        self.high = 0
        self.letter = None
        self.password = None
        self.parse()

    def parse(self):
        raw = self.raw.split()
        nums = raw[0].split("-")
        self.low, self.high = int(nums[0]), int(nums[1])
        self.letter = raw[1][0]
        self.password = raw[2]

    def is_valid(self):
        return sum([self.password[self.low-1] == self.letter, self.password[self.high-1] == self.letter]) == 1


file = open("input.txt", "r")
data = file.readlines()
file.close()

count = 0
total = 0
for line in data:
    thingy = Line(line)
    if thingy.is_valid():
        count += 1
    total += 1

print(count, total)

