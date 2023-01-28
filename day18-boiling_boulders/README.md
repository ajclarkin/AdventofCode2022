## Day 18 - Boiling Boulders

The input file is a series of x, y, z integers, each on a line. When using the usual list comprehension to read it they come in as strings.

Two options for reading them into a list of lists:

```python
    elements = [x for x in open('example.txt').read().strip().split('\n')]

    # Option 1
    for e in elements:
        print([int(v) for v in e.split(',')])


    # Option 2
    for e in elements:
        b = list(map(int, e.split(',')))
        print(b)

```

Option 1 is more pythonic.


### Part 1
Each line of input gives a 3d coordinates for 1x1x1 cubes - here referred to as boulders. Find the number of faces not immediately connected to another cube.

For example, 1,1,1 and 1,1,2 are adjacent. So we can see 5 faces of the former and 5 of the latter.

From the example code above we have a list called *boulders* with each cube in it.
 - Iterate through each boulder in the list and assign it 6 faces
 - Find the 6 adjacent positions and for each that is in *boulders* decrement faces by 1
 - Sum all the values of these faces counts

We create a new list containing the current boulder added on the the adjacent list (that is, with x-1, x+1, y-1 and so on) and then iterate through it checking if it's a boulder.


```python
adjacent = [
    [-1, 0, 0],
    [1, 0, 0],
    [0, -1, 0],
    [0, 1, 0],
    [0, 0, -1],
    [0, 0, 1]
]

adj_b = [list(map(sum, zip(b, a))) for a in adjacent]
    for a in adj_b:
        if a in boulders:
            f -= 1

```


### Part 2
This time we only want to count the faces which make up the external surface. It's possible that there are pockets within the structure which do not communicate with the outside and they should be excluded. (They won't be exposed to the steam in the scenario.)

The approach here is to identify every empty space in the 3d grid and check to see if it communicates with the edge of the grid. If it does not then it must be a pocket. So, for every black space do a breadth-first search, mapping out all the empties in communication with it. If any of them touch an edge then it's not a pocket.
 - If it's a pocket then save all the spaces within that pocket to a list for future comparison.
 - Save every space checked to a list called tested so that we don't re-check a space we already know about.

Once we have a list of all the pockets then follow the same approach as part one but this time exclude faces if they are adjacent to a boulder or pocket.

*Why it took me so long*
I made two errors. I initially thought about doing total faces from part 1 - faces of pockets. I got a seriously negative number. The other error is that I thought the grid went from 1 to max in each dimension rather than 0.
