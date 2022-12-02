# Day 2 - Rock Paper Scissors

This was a nice one, by which I mean I knew how to solve it.

Given an input file of the possible combinations of (A, B, C) and (X, Y, Z) which are supposed to
represent rounds of rock paper scissors, count the number of points based on a scoring system.

I used a dictionary for all the possible combinations and broke the score into value of hand played and outcome.
This made is easier for part 2 when the X|Y|Z became desired outcome rather than hand played.


```python
combo = {
    'AX': (3 + 1),
    'AY': (6 + 2),
    'AZ': (0 + 3),
    'BX': (0 + 1),
    'BY': (3 + 2),
    'BZ': (6 + 3),
    'CX': (6 + 1),
    'CY': (0 + 2),
    'CZ': (3 + 3)
}
```