# Day 03 - Rucksack Reorganisation, part 2
# Take 3 rows at a time and find the letter that is in each row.


input = [x for x in open('input.txt').read().split('\n')]
total = 0

for i in range(0, len(input), 3):
    found = set.intersection(set(input[i]), set(input[i+1]), set(input[i+2]))
    c = found.pop()
    total += (ord(c) - 38) if ord(c) < 97 else (ord(c) - 96)


print(f' The final total is {total}')
