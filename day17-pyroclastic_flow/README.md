# Day 17 - Pyroclastic Flow

## Part 1
I resorted to using an object for the wind to keep track of it between function calls and to save passing it
back and forth as parameters to functions. That worked quite nicely. I also used a reasonable number of list comprehensions
to make everything more efficient.

```python
# Generate the horizontal line
newshape = [(max_height+4, x) for x in range(2, 6)]


# Update every position tuple in a list to reduce the row coordinate by one
def DownShape(shape):
    return [(r-1, c) for r, c in shape]
```

I also found the `any()` function useful to check if any values are in two iterables:

```python
if any(coord in shape for coord in board):
    pass
```