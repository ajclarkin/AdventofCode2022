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


## Part 2
This was hard.

Find the height of the tower after a trillion blocks. This is not going to be brute force. I tried to find a relationship between the number of blocks added and the height. I rewrote part 1 to create a dataframe of number of blocks added against height and then delta height. I used a jupyter notebook to work through most of this. There is a roughly linear relationship (demonstrated by plotting blocks against height) but not perfect.


I tried to find a pattern in the blocks vs the change in height but to no avail. Because the blocks come in cycles of 5 I tried mod 5 for the blocks and the height. Eventually I tried a linear regression (including the direction of the wind as a categorical variable).

I looked to reddit for help and realised I had been on the right course. There is a repeating pattern in the change in height and this needs to be found. It doesn't start at zero. This was much easier to find in the example than the real input.

*Example*
The first 15 blocks don't contribute to the pattern.
Thereafter every 35 blocks add 53 to the height.

I found this by exporting blocks, height, and diff in height to a csv and then loading that in VSCode. By highlighting various digits in the diff_height and looking for patterns it became evident.



```python
height_first_15 = df[:16]['diff_h'].sum()

full_cycles = (1000000000000-15) // 35
height_full_cycles = full_cycles * 53

final_part_cycle = (1000000000000-15) % 35
height_final_part_cycle = df[16: (16+final_part_cycle)]['diff_h'].sum()

total = height_first_15 + height_full_cycles + height_final_part_cycle

```

This could be validated against the answer given.


*Real Input*
In principle the solution here is to do the same. Once again I could not find the pattern. Note that in the above example I did not include the actual wind (which is our example). I had tried but didn't need it. In the example the input is 40 characters long; in the real input it's 10091. I tried using it and finally didn't need it.

I had to find the pattern and couldn't. Eventually I guessed that it would be much longer. Instead of using the difference in height for each block added I looked at every cycle of 5 blocks added. I found the pattern eventually - it starts at 590 blocks and is 1760 blocks long. I found it looking at the height added with every 5 blocks.

Final working was the same but height of 2737 added for every 1760 blocks added, starting at block 590.

