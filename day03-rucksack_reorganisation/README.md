# Day 3 - Rucksack Reorganisation
Today we are sorting through elven bags - strings of upper and lower case characters.


## Part 1
Ok, I did this really inefficiently. Foe each line of the input we want to find the only character that appears
in both the left and right side.

I split the line into halves and then looped through the first half counting the number of occurences of each
character in the second. Only one character should appear on the other side so I bail out at this point. Initially
I was tripped up because the duplicate might be present more than once on each side so I break out of the loop once found.

*Better ways to do this*

I could have used a list comprehension or a set. See alternative.py for example of using a list comp.


Once we have found the character that appears in both sides we need to add it's value to the total.
I used ASCII values for this.
- A = 65, we want to correct to 27
- a = 97, we want to correct to 1

So, find the ASCII value and then convert it. If it's <97 then it's upper case otherwise lowercase:

`total += (ord(c) - 38) if ord(c) < 97 else (ord(c) - 96)`


## Part 2
I did this smarted - I used sets. Sets can't have duplicate values and are cannot be indexed (among other features). Best of all,
there is an `intersection()` method that finds the values in both or multiple sets.

We're looking at groups of three lines so `for` can do the looping and we'll specify jumping three each time.
Then we convert the 3 rows to sets, find the intersection - which returns a set - and then pop that value out of the set
so that we can convert to ASCII as above.

`found = set.intersection(set(input[i]), set(input[i+1]), set(input[i+2]))` where i is the loop control variable.