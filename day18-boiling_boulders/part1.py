# Day 18 - Boiling Boulders, part 1

elements = [x for x in open('input.txt').read().strip().split('\n')]
boulders = []

for e in elements:
    b = [int(v) for v in e.split(',')]
    boulders.append(b)

adjacent = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1]
]

faces = 0

for b in boulders:
    f = 6
    adj_b = [list(map(sum, zip(b, a))) for a in adjacent]
    for a in adj_b:
        if a in boulders:
            f -= 1

    faces += f

print(f'Total faces = {faces}')