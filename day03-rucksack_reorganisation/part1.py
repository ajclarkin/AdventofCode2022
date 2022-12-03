# Day 03 - Rucksack Reorganisation
# Find the duplicate character in each line
# Assign it a value 1-52
#   a-z = 1-26, A-Z = 27-52
# Sum the values


input = [x for x in open('input.txt').read().split('\n')]
total = 0

for i in input:
    item_len = int(len(i)/2)
    left, right = i[0:item_len], i[item_len:]


    # Loop throught the left hald looking for duplicate character in the right
    # The duplicate char can appear more than once so as soon as a match is found we break
    # ASCII a = 97, convert to 1; A = 65, convert to 27

    for c in left:
        if right.count(c) > 0:
            total += (ord(c) - 38) if ord(c) < 97 else (ord(c) - 96)
            break

print(f' The final total is {total}')
