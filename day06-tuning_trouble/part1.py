# Day 6 - Tuning Trouble, part 1
# Find the first place in the input text with 4 unique characters.
# Count to the end of that sequence

from collections import deque, Counter
# input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
input = open('input.txt').readline()

pos = 4
deq = deque(input[:4])

print(deq)

for c in input[4:]:
    pos += 1
    deq.popleft()
    deq.append(c)

    if len(Counter(deq)) == 4:
        break

print(f'Position found at {pos}')