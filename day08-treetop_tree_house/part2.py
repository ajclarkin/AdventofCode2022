# Day 8 - Treetop Tree House, part 2
from math import prod

input = [[int(char) for char in row] for row in open('input.txt').read().split('\n')]

distances = []
max_score = 0

move = {'U': -1, 'D': 1, 'L': -1, 'R': 1}


for row_no, row in enumerate(input):
    for col_no, char in enumerate(row):
        dist = 0
        pos = col_no
        blocked = False
        while pos != 0 and blocked == False:
            pos += move['L']
            dist += 1

            if input[row_no][pos] >= char:
                blocked = True
        
        distances.append(dist)


        # RIGHT
        dist = 0
        pos = col_no
        blocked = False
        while pos != (len(row)-1) and blocked == False:
            pos += move['R']
            dist += 1

            if input[row_no][pos] >= char:
                blocked = True
        
        distances.append(dist)        
        
        
        # UP
        dist = 0
        pos = row_no
        blocked = False
        while pos != 0 and blocked == False:
            pos += move['U']
            dist += 1

            if input[pos][col_no] >= char:
                blocked = True
        
        distances.append(dist)

        # DOWN
        dist = 0
        pos = row_no
        blocked = False
        while pos != (len(input)-1) and blocked == False:
            pos += move['D']
            dist += 1

            if input[pos][col_no] >= char:
                blocked = True
        
        distances.append(dist)     

        product = prod(distances)
        distances = []
        max_score = product if product > max_score else max_score



print(f'The maximum viewing score is {max_score}')