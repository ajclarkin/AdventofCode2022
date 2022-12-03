# Day 3 - Rucksack Reorganisation

## Part 1
Once we have found the character that appears in both sides we need to add it's value to the total.
I used ASCII values for this.
- A = 65, we want to correct to 27
- a = 97, we want to correct to 1

So, find the ASCII value and then convert it. If it's <97 then it's upper case otherwise lowercase:
`total += (ord(c) - 38) if ord(c) < 97 else (ord(c) - 96)`