# Day 14 - Regolith Reservoir

Parse directions to build walls within a grid. Then sand enters from the top and falls to the bottom.

I used an OOP approach to keep track of the walls and then the sand.

I had to decide how to store the data. I used tuples (x, y) for each wall unit or grain of sand and then when drawing the map I used two nested for loops to iterate through x and y. I was able to use `if (x, y) in self.map` to check for the presence of that tuple within the set.


# Part 1
Build up a set containing walls and then introduce the sand and keep a note of it's position too using a set.


## Part 2
This time there is an infinite width floor and so sand will keep falling until the nozzle where it enters is blocked. Factor this in. 

Pretty straight-forward but I needed to keep the left and right margins for the purposes of drawing the picture.