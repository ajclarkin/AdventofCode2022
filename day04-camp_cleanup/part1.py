# Day 4 - Camp Cleanup, part 1

import re

input = [x for x in open('input.txt').read().split('\n')]
count = 0

for i in input:
    l1, l2, r1, r2 = re.findall('[0-9]+', i)

    if (int(r1) >= int(l1) and int(r2) <= int(l2)) or (int(l1) >= int(r1) and int(l2) <= int(r2)):
      count += 1

print(f'Number of complete overlaps: {count}')