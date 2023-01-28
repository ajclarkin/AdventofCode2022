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
possibles = [[x, y, z] for x in range(1, max_x+1) for y in range(1, max_y+1) for z in range(1, max_z+1)]

max_possibles = len(possibles)
possibles_working = possibles.copy()
for p in possibles:
    if p in boulders:
        possibles_working.remove(p)
possibles = possibles_working.copy()

p_count = 0
for p in possibles:
    if p not in tested:
        # print(f'Testing {p}\t\t{len(pockets)} {len(not_pockets)}')
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
            if x == 1 or y == 1 or z == 1 or x == max_x or y == max_y or z == max_z:
                edge = True


            adj_b = [list(map(sum, zip(q, a))) for a in adjacent]
            for a in adj_b:
                if (0 < a[0] < max_x+1) and (0 < a[1] < max_y+1) and (0 < a[2] < max_z+1) \
                    and a not in current and a not in boulders and a not in queue and a not in tested:
                    queue.append(a)
        if edge == False:
            pockets.extend(current)
            p_count += 1
        else:
            not_pockets.extend(current)




faces = 0

for b in boulders:
    f = 6
    adj_b = [list(map(sum, zip(b, a))) for a in adjacent]
    for a in adj_b:
        if a in boulders or a in pockets:
            f -= 1

    faces += f




                
print('boulders', len(boulders))
print('pockets', len(pockets))
print('not_pockets', len(not_pockets))
print('max_possibles', max_possibles)
print('p_count', p_count)
print('faces', faces)
print('tested', len(tested))

print()

s1 = set()
for p in not_pockets:
    x,y,z = p
    s1.add((x, y, z))

print(set, len(s1))


# 2096 too high