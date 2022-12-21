# Day 12 - Hill Climbing Algorithm
from collections import deque

# Read the input into a dict of format dict[(row_no, col_no)] : letter
rows = [line for line in open('input.txt').read().split('\n')]
hill = {(rk, ck): cv for rk, rv in enumerate(rows) for ck, cv in enumerate(rv)}
visited = set()
parents = {}

paths = list()
start = [k for k,v in hill.items() if v == 'S'][0]
paths.append(start)

end = [k for k,v in hill.items() if v == 'E'][0]

hill.update({start: 'a'})
hill.update({end: 'z'})

def CheckNewPosition(hill, current, visited, move):
    if move == 'U':
        newpos = (current[0]-1, current[1])
    elif move == 'D':
        newpos = (current[0]+1, current[1])
    elif move == 'L':
        newpos = (current[0], current[1]-1)
    elif move == 'R':
        newpos = (current[0], current[1]+1)

    if newpos in hill and newpos not in visited:
        if ord(hill[newpos]) < (ord(hill[current])+2):
            return newpos
        else:
            return None

for pos in paths:
    visited.add(pos)

    for direction in ['U', 'D', 'L', 'R']:
        newpos = CheckNewPosition(hill, pos, visited, direction)
        if newpos is not None and newpos not in paths:
            parents.update({newpos: pos})
            paths.append(newpos)

        if newpos == end:
            break


# Now work our way backwards
steps = 0
current = end
while current != start:
    steps += 1
    current = parents[current]

print(f'Total number of moves: {steps}')