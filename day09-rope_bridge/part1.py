# Day 9 - Rope Bridge, part 1

input = [x for x in open('input.txt').read().split('\n')]
head = {'x': 0, 'y': 0}
tail = {'x': 0, 'y': 0}

dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
dy = {'U': -1, 'D': 1, 'L': 0, 'R': 0}

y_positions = set()
y_positions.add((tail['x'], tail['y']))

for i in input:
    words = i.split()
    for movement in range(int(words[1])):
        head['x'] += dx[words[0]]
        head['y'] += dy[words[0]]

        diff_x = head['x'] - tail['x']
        diff_y = head['y'] - tail['y']

        if diff_x == 2:
            tail['x'] += dx['R']
        
        if diff_x == -2:
            tail['x'] += dx['L']

        if abs(diff_x) == 2:

            if diff_y == 1:
                tail['y'] += dy['D']
            if diff_y == -1:
                tail['y'] += dy['U']



        if diff_y == 2:
            tail['y'] += dy['D']

        if diff_y == -2:
            tail['y'] += dy['U']

        if abs(diff_y) == 2:
            if diff_x == 1:
                tail['x'] += dx['R']
            if diff_x == -1:
                tail['x'] += dx['L']

        y_positions.add((tail['x'], tail['y']))


print(f'Y positions = {len(y_positions)}')