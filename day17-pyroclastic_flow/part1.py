# Day 17 - Pyroclastic Flow, part 1
# It's bloody tetris.

# Input defines the movements left or right
# Standard sequence of block addition and initial placement

from operator import itemgetter


max_height = 0


# Board will be the map of everything no longer moving. Include the floor.
# Each block will be (row, column) and floor will be row 0.
board = set()
board.update([(0, x) for x in range(7)])
max_height = 0


class Wind:
    '''
        Use this to track the state of the wind and keep state between function calls
    '''
    def __init__(self) -> None:
        self.wind = [x for x in open('input.txt').read().strip()]
        self.wind_pos = 0
        self.wind_len = len(self.wind)


    def GetWind(self):
        if self.wind[self.wind_pos] == '<':
            ret = -1
        else:
            ret = 1

        self.wind_pos = self.wind_pos + 1 if (self.wind_pos +1) < self.wind_len else 0
        return ret



def NewShape(pattern, max_height):
    '''
    Create a list with the positions of each block making up the new shape.
    Use an int to track which shape gets added next, 0-4:
        - + _| | #
    '''
    newshape = []

    if pattern == 0:
        # horizontal line
        newshape = [(max_height+4, x) for x in range(2, 6)]

    if pattern == 1:
        # plus sign
        newshape = [(max_height+4+1, x) for x in range(2, 5)]
        newshape.extend([(max_height+4+x, 3) for x in range(0,3,2)])

    if pattern == 2:
        # reverse L
        newshape = [(max_height+4, x) for x in range(2, 5)]
        newshape.extend([(max_height+4+x, 4) for x in range(1, 3)])


    elif pattern == 3:
        # vertical line
        newshape = [(max_height+4+x, 2) for x in range(4)]

    elif pattern == 4:
        # 2x2 square
        newshape = [(max_height+4+r, c+2) for r in range(2) for c in range(2)]

    return newshape



def BlowShape(shape, direction, board):
    '''
    Direction will be -1 if < and 1 if >
    '''

    temp = shape.copy()
    shape = [(r, c + direction) for r, c in shape]

    if (min(shape, key=itemgetter(1))[1] < 0) or (max(shape, key=itemgetter(1))[1] > 6) or any(coord in shape for coord in board):
        return temp
    else:
        return shape

    


def DownShape(shape):
    return [(r-1, c) for r, c in shape]



def PrintBoard(board):
    top = max(board, key=itemgetter(0))[0] + 2

    for r in range(top, -1, -1):
        print('|', end = '')
        for c in range(7):
            if (r, c) in board:
                print('#', end = '')
            else:
                print('.', end='')
        print('|')

    print()
    print()
        



wind = Wind()


for i in range(2022):

    shape = NewShape(i%5, max_height)
    can_move = True

    while can_move:

        shape = BlowShape(shape, wind.GetWind(), board)
        temp = shape.copy()
        shape = DownShape(shape)

        if any(coord in shape for coord in board):
            can_move = False
            board.update(temp)

    max_height = max(board)[0]

    # PrintBoard(board)


print(f"The maximum height is {max_height}")
