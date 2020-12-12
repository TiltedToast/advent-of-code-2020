file = open('input.txt', 'r')
lines = file.readlines()

lines = [int(line.replace('\n', '')) for line in lines]

i = 25
try_number = 0
try_sum = 0
while i < len(lines):
    try_number = lines[i]
    try_range = lines[i - 25:i]
    found_match = False
    for number in try_range:
        if try_number > number:
            try_match = try_number - number
            if try_match in try_range:
                found_match = True
                continue
    if found_match is False:
        print(f"Found it! {lines[i]}")
        break
    i += 1

working_range = []
for i, start_number in enumerate(lines):
    working_range = [start_number]
    try_sum = try_number
    try_range = lines[i + 1:]
    for next_number in try_range:
        try_sum -= next_number
        if try_sum < 0:
            continue
        elif try_sum == 0:
            working_range.append(next_number)
            break
        elif try_sum > 0:
            working_range.append(next_number)
    if try_sum == 0:
        break

print(try_number, max(working_range) + min(working_range))