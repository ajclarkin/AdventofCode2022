# Day 4 - Camp Cleanup, part 2

import re

input = [x for x in open('input.txt').read().split('\n')]
count = 0

for i in input:
    l1, l2, r1, r2 = re.findall('[0-9]+', i)

    l1 = int(l1)
    l2 = int(l2)
    r1 = int(r1)
    r2 = int(r2)

    if (l1<=r1<=l2) or (l1<=r2<=l2) or (r1<=l1<=r2) or (r1<=l2<=r2):
      print(i)
      count += 1

print(f'Number of partial overlaps: {count}')