table = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}

with open('input.txt', 'r') as f:
    seats = [int(''.join(table[c] for c in line.strip()), 2) for line in f]
    print(f'Part 1: {max(seats)}')
    for id in range(max(seats)):
        if id not in seats and id - 1 in seats and id + 1 in seats:
            print(f'Part 2: {id}')
            break