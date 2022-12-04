# Day 4 - Camp Cleanup
Today was pretty easy. Given a file of ranges like 
> 22-28,25-30
we're looking for overlaps.

I used a regular expression to pull the values out - and then intially forgot to cast then to int.

```python
l1, l2, r1, r2 = re.findall('[0-9]+', input_line)
```

## Part 1 - Complete Overlaps
Looking for one side being completely within the other. 
> 10-20,15-16


## Part 2 - Partial Overlaps
In this round there just had to be on overlap but one side not need to be wholly contained:
> 10-20,9-13

I only just discovered that you can do `if (value1 <= x <= value2):` so that was helpful.