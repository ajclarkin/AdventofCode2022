# Day 9 - Rope Bridge
Typical advent of code. The ones you read and thing "I can't do this" are a pleasant challenge, the "No bother..." ones are a nightmare. This was the former.

## Part 1
This uses dictionaries to store the x and y coordinates for the head and tail. Each time the head moves we compare the position between
head and tail and then move the tail if appropriate.


## Part 2
Here we have head and then another 9 knots. Each knot depends on the previous one and moves in the same way as in part 1. So, we
use a `Knot` class and then each knot becomes an object. This seems almost like the classic example of what an object is when reading about
OOP.

We save the positions of knot 9 to a set to de-duplicate then count the entries.
