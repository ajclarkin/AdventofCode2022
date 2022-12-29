# Day 15 - Beacon Exclusion Zone
# Each sensor has a radius defined by the distance to the nearest sensor.
# Find how many empty squares there are on row 2000000 (row 10 for example)

import re


lines = [x for x in open('input.txt').read().strip().split('\n')]
line_y = 2000000
line_y_fill = set()

for l in lines:
    # sensor and beacon columns and rows
    sc, sr, bc, br = map(int, re.findall('-?\d+', l))

    dr = abs(sr-br)
    dc = abs(sc-bc)
    d_tot = dr + dc

    # Calculate the squares on line_y that this sensor covers
    # That will be (d_tot - vertical distance) either side of the column coordinate

    vertical = abs(sr - line_y)
    d_rem = d_tot - vertical

    if d_tot >= vertical:
        for col in range((sc-d_rem), (sc+d_rem+1)):
            # remember to take out the beacon
            if not(br == line_y and bc == col):
                line_y_fill.add(col)

print(f'There are {len(line_y_fill)} boxes which cannot contain a beacon')