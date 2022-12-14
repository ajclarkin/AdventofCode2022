# Day 9 - Rope Bridge, part 1
# Use Knot class to store the position of each knot.
# Head will be knot[0]

input = [x for x in open('input.txt').read().split('\n')]
head = {'x': 0, 'y': 0}

dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
dy = {'U': -1, 'D': 1, 'L': 0, 'R': 0}



class Knot():
    def __init__(self):
        self.position = {'x': 0, 'y': 0}
        self.dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
        self.dy = {'U': -1, 'D': 1, 'L': 0, 'R': 0}


    def SetPosition(self, axis, position):
        self.position[axis] = position


    def MoveFollower(self, front_x, front_y):
        # Given the new position of the knot in front make the appropriate move if required        diff_x = head['x'] - tail['x']
        diff_x = front_x - self.position['x']
        diff_y = front_y - self.position['y']

        if diff_x == 2:
            self.position['x'] += self.dx['R']
        
        if diff_x == -2:
            self.position['x'] += self.dx['L']

        if abs(diff_x) == 2:

            if diff_y == 1:
                self.position['y'] += self.dy['D']
            if diff_y == -1:
                self.position['y'] += self.dy['U']



        if diff_y == 2:
            self.position['y'] += self.dy['D']

        if diff_y == -2:
            self.position['y'] += self.dy['U']

        if abs(diff_y) == 2:
            if diff_x == 1:
                self.position['x'] += self.dx['R']
            if diff_x == -1:
                self.position['x'] += self.dx['L']




    def GetPosition(self):
        return self.position['x'], self.position['y']

knots = [Knot() for k in range(10)]
tail_positions = set()


for i in input:
    words = i.split()
    for movement in range(int(words[1])):
        head['x'], head['y'] = knots[0].GetPosition()

        head['x'] += dx[words[0]]
        head['y'] += dy[words[0]]

        knots[0].SetPosition('x', head['x'])
        knots[0].SetPosition('y', head['y'])


        for i in range(1, 10):
            knots[i].MoveFollower(knots[i-1].position['x'], knots[i-1].position['y'])

        tail_positions.add(knots[9].GetPosition())


print(f'Knot number 9 visits {len(tail_positions)} positions')