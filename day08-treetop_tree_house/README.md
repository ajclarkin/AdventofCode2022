# Day 8 - Treetop Tree House
I read it and saw how to solve it quite quickly. Then I made it look difficult.

Two different problems from a grid a trees, the first to find the number of trees visible from outside the grid 
based on their height and the second to calculate the number of trees visible in each direction from each tree and to find the product of those values.


## Part 1
For each row I go along from left to right and then back and look to see if it is the highest value between the current position
and the outside. On the way back I stop when I reach the high point of the outward journey.

I do this for each row and column except those on the perimeter (and exclude high trees on the perimeter) then add the total
number of trees on the perimeter.

I didn't read the instructions properly. This will double-count trees if they are visible from two different directions such 
as left and down. So, instead I save a tuple of tree coordinates to a set and then count the length of the set to find number of trees at the end.


## Part 2
This time for each tree count the number of trees visible in each direction. The line of site stops at a tree of equal height (or greater).

So, instead of looking along rows and columns for trees we're starting at trees and seeing how far we can see along corresponding rows 
and columns.

Untidy code - 4 copies of effectively the same logic. For each x,y position I repetitively move L, R, U, D to find the number of trees visible. Then the score is calculated from the product of these 4 values and if it's higher than the last recorded score then keep it. Otherwise I move on.