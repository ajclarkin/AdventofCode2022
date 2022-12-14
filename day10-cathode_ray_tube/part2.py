# Day 10 - Cathode Ray Tube, part 1

input = [line for line in open('input.txt').read().split('\n')]
cycle = 1
register = 1


def DrawPixel(cycle, register):
    # Register counts from 0 to 39, cycle from 1 to 40
    # Deal with this by keeping cycle in this range and adding 1 to register (that is range reg-1:reg+1 becomes reg:reg+2)
    if (register) <= cycle%40 <= (register+2):
        print('#', end='')
    else:
        print('.', end='')

    if cycle % 40 == 0:
        print()


for row_no, row in enumerate(input):
    words = row.split()

    if words[0] == 'noop':
        DrawPixel(cycle, register)
        cycle += 1
    else:
        DrawPixel(cycle, register)
        cycle += 1
        DrawPixel(cycle, register)
        cycle += 1
        register += int(words[1])
        
