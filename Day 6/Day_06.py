group_answers = [list(line.split()) for line in open('input.txt').read().split('\n\n')]

part1_answers = 0
part2_answers = 0

for group in group_answers:
    valid_answers = []
    for person in group:
        valid_answers += list(person)
    totality = [1 for x in set(valid_answers) if valid_answers.count(x) == len(group)]
    part1_answers += len(set(valid_answers))
    part2_answers += (sum(totality))

print(f'Part 1: {part1_answers}')
print(f"Part 2: {part2_answers}")