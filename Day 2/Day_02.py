lines = [line for line in open("input.txt")]

total_1 = 0
total_2 = 0

for i in range(len(lines)):
    min_count = int(lines[i].split("-")[0])
    max_count = int(lines[i].split()[0].split("-")[1])
    character = lines[i].split(":")[0][-1]
    password = lines[i].split()[-1]

    if min_count <= password.count(character) <= max_count:
        total_1 += 1

    if password[min_count-1] == character or password[max_count-1] == character:
        if not (password[min_count-1] == character and password[max_count-1] == character):
            total_2 += 1


print(total_1)
print(total_2)




