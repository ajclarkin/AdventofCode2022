# Day 01 - Calorie Counting
It's nice to be back at the start. Today's puzzles were pretty easy although part 2 tripped me up: **always check your input**.

## Part 1
Given a list of integers broken up by spaces. Calculate the total for each block then find the biggest total.

I dare say I could have used some advanced library but it seemed like overkill. Solution: loop through the input adding while not blank line. Then use max() to find the biggest.


## Part 2
Now find the three biggest. Easy. `list.sort(reverse=True)[0:3]`
Of course, that didn't give me a big enough answer. Once I re-checked my input and re-ran it everything was fine.

Mr Wastl doesn't make mistakes: you do.