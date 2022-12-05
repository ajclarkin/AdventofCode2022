# Day 5 - Supply Stacks, part 2
# This time the order is retained when moving more than one crate


import re

stacks = [
    [],
    ['Z', 'P', 'M', 'H', 'R'],
    ['P', 'C', 'J', 'B'],
    ['S', 'N', 'H', 'G', 'L', 'C', 'D'],
    ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
    ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
    ['T', 'F', 'S', 'Z', 'B', 'G'],
    ['N', 'R', 'V'],
    ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
    ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
]


moves = [x for x in open('moves.txt').read().split('\n')]

for m in moves:
    crates, stack_from, stack_to = re.findall('[0-9]+', m)
    crates = int(crates)
    stack_from = int(stack_from)
    stack_to = int(stack_to)

    if crates == 1:
        c = stacks[stack_from].pop()
        stacks[stack_to].append(c)
    else:
        for i in range(crates, 0, -1):
            c = stacks[stack_from].pop(-i)
            stacks[stack_to].append(c)


for j in range(1, 10):
    print(f'{stacks[j][-1]}', end='')