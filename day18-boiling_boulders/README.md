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