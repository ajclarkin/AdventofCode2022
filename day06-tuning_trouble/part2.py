# Day 6 - Tuning Trouble, part 2
# Find the first place in the input text with 14 unique characters.
# Count to the end of that sequence

from collections import deque, Counter
input = open('input.txt').readline()

pos = 14
deq = deque(input[:14])

if len(Counter(deq)) == 14:
    print('Value found immediately at 14')

for c in input[14:]:
    pos += 1
    deq.popleft()
    deq.append(c)

    if len(Counter(deq)) == 14:
        break

print(f'Position found at {pos}')