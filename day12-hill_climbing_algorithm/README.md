# Day 12 - Hill Climbing Algorithm

Find a path from the bottom of the hill to the top where you only climb one unit of altitude - or descend as many as you want - with each step. Should be easy - I know this is a breadth-first search. I know about queues, deques, and visit histories. I wrestled with this for ages [Advent of Code 2019, Day 15](https://github.com/ajclarkin/AdventofCode2019/tree/master/day15).

So I wrote a solution which tracks every possible path until it finds the end point. It worked fine for the example. It did not work for the input. Not sure why but on debugging I can see the number of paths being tracked just going up and up and up. I've kept it here  [part1_all-paths.py](part1_all-paths.py) for reference.


## Part 1
For the working version I just work through a classic (I think) graph traversal adding each subsequent node to the queue and keeping a note of every node visited so I don't repeat. This stops when I reach the end point.

To calculate the distance I use a dictionary called parents where the key is the child node and the value is the parent node. This means that once I have the end point in this dict I can work my way back through the dictionary counting steps. It feels like there should probably be a better way though.


```python
steps = 0
current = end
while current != start:
    steps += 1
    current = parents[current]
```


## Part 2
Now find the shortest path from altitude 'a' to the end point. I reworked the code to work backwards from the endpoint until it finds an 'a' - that will be the nearest. Same approach as part 1.
