# Day 15 - Beacon Exclusion Zone, part 2
# There is a beacon that is not detected by any sensor. There is only one single position that it can be in.
# The grid system is 0 to 4e6 on both x and y axis.
# Find the only point it could be at. Multiply the x (column) value by 4e6 and add the y value.


import re


lines = [x for x in open('input.txt').read().strip().split('\n')]
sensors = dict()

for l in lines:
    # sensor and beacon columns and rows
    sc, sr, bc, br = map(int, re.findall('-?\d+', l))

    dr = abs(sr-br)
    dc = abs(sc-bc)
    d_tot = dr + dc

    sensors.update({(sc, sr): d_tot})




def CheckManhattanDistance(c, r, sensors):
    '''
    Checks a coordinate against every sensor's distance. If within a sensor distance then it cannot be
    the coordinate we're looking for - return false.
    Otherwise return true.
    '''

    if not ((0 <= c <= 4e6) and (0 <= r <= 4e6)):
        return False

    for k, dist in sensors.items():
        sc, sr = k
        dr = abs(sr-r)
        dc = abs(sc-c) 
        d_tot = dr + dc

        if d_tot <= dist:
            return False
    return True





def FindBoundary(k, dist, sensors):
    '''
    For a given sensor find all the surrounding squares which are manhattan distance + 1.
    Start at 12 o'clock and and work clockwise.
    '''
    dist += 1
    c, r = k
    dc, dr = 0, -dist

    while dr < 0:
        if CheckManhattanDistance(c + dc, r + dr, sensors):
            print(f'The beacon coordinates are ({c + dc, r + dr})')
            return ((c+dc)*4e6 + r+dr)
        dr += 1
        dc +=1

    while dc > 0:
        if CheckManhattanDistance(c + dc, r + dr, sensors):
            print(f'The beacon coordinates are ({c + dc, r + dr})')
            return ((c+dc)*4e6 + r+dr)
        dr += 1
        dc -=1

    while dr > 0:
        if CheckManhattanDistance(c + dc, r + dr, sensors):
            print(f'The beacon coordinates are ({c + dc, r + dr})')
            return ((c+dc)*4e6 + r+dr)
        dr -= 1
        dc -=1

    while dc < 0:
        if CheckManhattanDistance(c + dc, r + dr, sensors):
            print(f'The beacon coordinates are ({c + dc, r + dr})')
            return ((c+dc)*4e6 + r+dr)
        dr -= 1
        dc +=1
    return False


# Work round every sensor and check each position 1 unit outside it's range to see if it falls within any other sensor range
# If it doesn't then that's the sensor we're looking for.

for k, dist in sensors.items():
    c, r = k
    if (res := FindBoundary((c, r), dist, sensors)):
        print(f'The final result is {int(res)}')
        break

