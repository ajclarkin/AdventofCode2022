# Day 12 - Hill Climbing Algorithm, part 2
# This time lets do it backwards until we find a location of height 'a'

# Read the input into a dict of format dict[(row_no, col_no)] : letter
rows = [line for line in open('input.txt').read().split('\n')]
hill = {(rk, ck): cv for rk, rv in enumerate(rows) for ck, cv in enumerate(rv)}
visited = set()
parents = {}

paths = list()
start = [k for k,v in hill.items() if v == 'E'][0]
paths.append(start)

# Keep the old start position in (as end) to ensure we consider it
end = [k for k,v in hill.items() if v == 'S'][0]
hill.update({start: 'z'})
hill.update({end: 'a'})


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
        if ord(hill[newpos]) > (ord(hill[current])-2):
            return newpos
        else:
            return None

first_a = None
stop_search = False
for pos in paths:
    visited.add(pos)

    for direction in ['U', 'D', 'L', 'R']:
        newpos = CheckNewPosition(hill, pos, visited, direction)
        if newpos is not None and newpos not in paths:
            parents.update({newpos: pos})
            paths.append(newpos)

        if newpos is not None and hill[newpos] == 'a':
            print('Found A')
            first_a = newpos

    if first_a is not None:
        break


# Now work our way backwards
steps = 0
current = first_a
print(current, start)
while current != start:
    steps += 1
    current = parents[current]

print(f'Total number of moves: {steps}')