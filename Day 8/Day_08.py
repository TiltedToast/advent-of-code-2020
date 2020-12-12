from copy import deepcopy


def solve(instructions):

    # setup vars to track
    acc = 0
    pos = 0
    visited = set()

    while True:
        if pos == len(instructions) or pos in visited:
            break
        else:
            visited.add(pos)

        # parse out operation and argument
        item = instructions[pos]
        op = item.split(' ')[0]
        arg = int(item.split(' ')[1])

        if op == 'acc':
            acc += arg
            pos += 1
        if op == 'jmp':
            pos += arg
        if op == 'nop':
            pos += 1

    # return final position and accumulator
    return pos, acc


# read in aoc input
instructions = open("input.txt").read().strip().split('\n')

# solve for part 1
p1 = solve(instructions)
print(f'Part 1: {p1[1]}')

# solve for part 2
for n, item in enumerate(instructions):
    op = item.split(' ')[0]

    # check to see if change needs to be made
    if op == 'nop' or op == 'jmp':
        new_instructions = deepcopy(instructions)

        # make change to new instruction set
        if op == 'nop':
            new_instructions[n] = 'jmp' + new_instructions[n][3:]
        if op == 'jmp':
            new_instructions[n] = 'nop' + new_instructions[n][3:]

        # submit new instruction set to solve function
        p2 = solve(new_instructions)

        # if final position is vlaid end loop
        if p2[0] == len(instructions):
            break
    else:
        continue

print(f'Part 2: {p2[1]}')