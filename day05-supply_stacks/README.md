# Day 5 - Supply Stacks

I didn't know what to do with the input today - it was in two parts. I ended up typing up the stacks at the top manually which took
a while. I'm sure there must have been a better way to do it.

The moves are parsed out of the new input file (moves.txt) and converted to int. Same as yesterday - regexs.


## Part 1
The stacks of crates are represented by lists. Each move is a pop from one stack and an append to the other.


## Part 2
Now when moving more than one crate they are moved in bulk and so keep their order. I pop them in the order they need to be appended to the new list in. For example, if moving 3 crates I pop(-3), pop(-2), pop(-1), appending each time.
