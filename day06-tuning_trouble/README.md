# Day 6 - Tuning Trouble
Starts with hints about the intcode computer from 2019 and the flawed requency transmission that's still bothering me.

Easy one this. The input is a long string of characters. We have to find the first position where there are 4 unique characters in a row. For the second part it's just finding 14 characters in a row.

I used `collections.deque()` for this. A double-ended list. I loaded it with the first 4 characters and then moved that 4 character reading frame down the input - popping a character from the left and appending one at the right. With each change of character I used `collections.Counter()` to count the elements. If the length of the counter didn't equal 4 (or 14 in part 2) then I moved on.

I kept a position counter along the way so I knew where I was.