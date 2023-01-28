# Day 18 - Boiling Boulders, part 2

from collections import deque

elements = [x for x in open('input.txt').read().strip().split('\n')]
boulders = []
max_x, max_y, max_z = 0, 0, 0

queue = deque()
tested = []
pockets = []
not_pockets = []
part_1 = 3526


adjacent = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1]
]

for e in elements:
    b = [int(v) for v in e.split(',')]
    boulders.append(b)

    x, y, z = b
    max_x = x if x > max_x else max_x
    max_y = y if y > max_y else max_y
    max_z = z if z > max_z else max_z

print(max_x, max_y, max_z)

# Find all the blocks excluding those on the perimeter
possibles = [[x, y, z] for x in range(2, max_x) for y in range(2, max_y) for z in range(2, max_z)]

for p in possibles:
    if p in boulders:
        possibles.remove(p)


for p in possibles:
    if p not in tested:
        # print(f'Testing {p}\t\t{len(pockets)} {len(not_pockets)}')
        current = []
        queue.clear()

        queue.append(p)
        edge = False

        while (len(queue) > 0) and (edge == False):
            q = queue.popleft()
            current.append(q)
            tested.append(q)

            # Check if it's at the edge
            x, y, z = q
            if x == 1 or y == 1 or z == 1 or x == max_x or y == max_y or z == max_z:
                edge = True

            if edge == False:
                adj_b = [list(map(sum, zip(q, a))) for a in adjacent]
                for a in adj_b:
                    if a not in current and a not in boulders and a not in queue:
                        queue.append(a)
            
        if edge == False:
            pockets.append(current)
        else:
            not_pockets.extend(current)


# print(f'Pockets {pockets}')
# print(f'Not Pockets {not_pockets}')

faces_p, faces_np = 0, 0

# Unpack pockets
flat_pockets = []
for p in pockets:
    flat_pockets.extend(p)



for p in flat_pockets:
    f = 6
    adj_b = [list(map(sum, zip(p, a))) for a in adjacent]
    for a in adj_b:
        if a in pockets:
            f -= 1
    faces_p += f


# for np in not_pockets:
#     f = 6
#     adj_b = [list(map(sum, zip(np, a))) for a in adjacent]
#     for a in adj_b:
#         if a in not_pockets:
#             f -= 1

#     faces_np += f

# print(f'Total faces = {faces_np}')
print(f'Total pocket faces = {faces_p}')
print(f'Answer = {3526 - faces_p}')
                
