# Day 18 - Boiling Boulders, part 2

from collections import deque

elements = [x for x in open('input.txt').read().strip().split('\n')]
boulders = []
max_x, max_y, max_z = 0, 0, 0

for e in elements:
    b = [int(v) for v in e.split(',')]
    boulders.append(b)

    x, y, z = b
    max_x = x if x > max_x else max_x
    max_y = y if y > max_y else max_y
    max_z = z if z > max_z else max_z



queue = deque()
tested = []
pockets = []


adjacent = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1]
]


# Identify every possible block space
possibles = [[x, y, z] for x in range(max_x+1) for y in range(max_y+1) for z in range(max_z+1)]


# From the possible blocks we want to remove those which contain boulders.
# We can't edit the list while iterating through it so we use a copy.

possibles_working = possibles.copy()
for p in possibles:
    if p in boulders:
        possibles_working.remove(p)
possibles = possibles_working.copy()



# Find all the pockets - those non-boulder areas completely surrounded by boulders.
# This is a repeated breadth-first search.

for p in possibles:
    if p not in tested:
        current = []
        queue.clear()

        queue.append(p)
        edge = False

        while len(queue) > 0:
            q = queue.popleft()
            current.append(q)
            tested.append(q)

            # Check if it's at the edge
            x, y, z = q
            if x == 0 or y == 0 or z == 0 or x == max_x or y == max_y or z == max_z:
                edge = True


            adj_b = [list(map(sum, zip(q, a))) for a in adjacent]
            for a in adj_b:
                if 0 <= a[0] < max_x+1 and 0 <= a[1] < max_y+1 and 0 <= a[2] < max_z+1 \
                    and a not in current and a not in boulders and a not in queue:
                    queue.append(a)

        if edge == False:
            pockets.extend(current)



faces = 0

for b in boulders:
    f = 6
    adj_b = [list(map(sum, zip(b, a))) for a in adjacent]
    for a in adj_b:
        if a in boulders or a in pockets:
            f -= 1

    faces += f

                
print('Faces', faces)
