# Day 12 - Hill Climbing Algorithm
from collections import deque

# Read the input into a dict of format dict[(row_no, col_no)] : letter
rows = [line for line in open('example.txt').read().split('\n')]
hill = {(rk, ck): cv for rk, rv in enumerate(rows) for ck, cv in enumerate(rv)}
visited = set()

paths = deque()
start = [k for k,v in hill.items() if v == 'S']
paths.append(start)

start = start[0]
end = [k for k,v in hill.items() if v == 'E'][0]

hill.update({start: 'a'})
hill.update({end: 'z'})


p = paths.popleft()
current = p[-1]

while current != end:
    visited.add(current)
    height = hill[current]

    if ((current[0]-1, current[1]) in hill) and (ord(hill[(current[0]-1, current[1])]) < (ord(height)+2)) and ((current[0]-1, current[1]) not in visited):
        temp = p.copy()
        temp.append((current[0]-1, current[1]))
        paths.append(temp)

    if ((current[0]+1, current[1]) in hill) and (ord(hill[(current[0]+1, current[1])]) < (ord(height)+2)) and ((current[0]+1, current[1]) not in visited):
        temp = p.copy()
        temp.append((current[0]+1, current[1]))
        paths.append(temp)

    if ((current[0], current[1]-1) in hill) and (ord(hill[(current[0], current[1]-1)]) < (ord(height)+2)) and ((current[0], current[1]-1) not in visited):
        temp = p.copy()
        temp.append((current[0], current[1]-1))
        paths.append(temp)

    if ((current[0], current[1]+1) in hill) and (ord(hill[(current[0], current[1]+1)]) < (ord(height)+2)) and ((current[0], current[1]+1) not in visited):
        temp = p.copy()
        temp.append((current[0], current[1]+1))
        paths.append(temp)


    p = paths.popleft()
    current = p[-1]


    if len(paths) == 1000:
        for k in visited:
            print(hill[k], end='')

        break




print(f'Solution: {len(p)-1} steps')
