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