# Day 14 - Regolith Reservoir, part 2
# Now we need to add a floor and then work out when the sand nozzle (at 500,0) get blocked                                                              


class Cave:
    def __init__(self) -> None:
        self.walls = [x for x in open('input.txt').read().split('\n')]
        self.map = set()
        self.sand = set()

        self.x_max = 500
        self.x_min = 500

        self.y_max = 0
        self.y_min = 0

        for self.w in self.walls:
            self.start, self.end = '', ''
            for self.end in self.w.split(' -> '):
                if self.start != '':
                    self.BuildWall(self.start, self.end)
                self.start = self.end


    def BuildWall(self, start, end):
        '''
        Populate the set self.map with every coordinate for a wall.
        Keep a note of the edges of the map
        '''
        self.x_end, self.y_end = self.end.split(',')
        self.x_start, self.y_start = self.start.split(',')

        self.x_start = int(self.x_start)
        self.x_end = int(self.x_end)
        self.y_start = int(self.y_start)
        self.y_end = int(self.y_end)


        self.map.add((self.x_start, self.y_start))
        self.x_max = self.x_start if self.x_start > self.x_max else self.x_max
        self.x_min = self.x_start if self.x_start < self.x_min else self.x_min
        self.y_max = self.y_start if self.y_start > self.y_max else self.y_max
        self.y_min = self.y_start if self.y_start < self.y_min else self.y_min


        while self.x_start != self.x_end:
            self.x_start = (self.x_start + 1) if self.x_start < self.x_end else (self.x_start - 1)
            self.map.add((self.x_start, self.y_start))

            self.x_max = self.x_start if self.x_start > self.x_max else self.x_max
            self.x_min = self.x_start if self.x_start < self.x_min else self.x_min


        while self.y_start != self.y_end:
            self.y_start = (self.y_start + 1) if self.y_start < self.y_end else (self.y_start - 1)
            self.map.add((self.x_start, self.y_start))

            self.y_max = self.y_start if self.y_start > self.y_max else self.y_max
            self.y_min = self.y_start if self.y_start < self.y_min else self.y_min


    def AddSand(self):
        '''
            Add a particle of sand and see where it ends up
        '''

        self.sand_x = 500
        self.sand_y = 0

        move = True
        while move:
            if (self.sand_x, self.sand_y+1) not in self.map and (self.sand_x, self.sand_y+1) not in self.sand and (self.sand_y+1 < self.y_max +2):
                self.sand_y += 1
            elif (self.sand_x-1, self.sand_y+1) not in self.map and (self.sand_x-1, self.sand_y+1) not in self.sand and (self.sand_y+1 < self.y_max +2):
                self.sand_x -= 1
                self.sand_y += 1
            elif (self.sand_x+1, self.sand_y+1) not in self.map and (self.sand_x+1, self.sand_y+1) not in self.sand and (self.sand_y+1 < self.y_max +2):
                self.sand_x += 1
                self.sand_y += 1
            else:
                # Cannot make a move
                move = False


        self.sand.add((self.sand_x, self.sand_y))
        if self.sand_x == 500 and self.sand_y == 0:
            return False
        else:
            return True






    def DrawMap(self):
        for y in range(self.y_min, self.y_max+1, 1):
            for x in range(self.x_min, self.x_max+1, 1):
                if (x, y) in self.map:
                    print('#', end='')
                elif (x, y) in self.sand:
                    print('o', end='')
                else:
                    print('.', end='')

            print()



cave = Cave()

while cave.AddSand():
    pass

cave.DrawMap()

print()
print(f'Total grains of sand: {len(cave.sand)}')