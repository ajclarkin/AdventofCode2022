# Day 11 - Monkey in the Middle
A more complicated data structure to parse from the input today:


```
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3


```

I start by breaking it into chunks, each chunk a monkey, by splitting at the double newline. Then just work through linewise pulling
out the values required. There was lots of casting to int required. I use a list of Monkey classes to keep track and can then loop through them.

For the operator in the operation line:

```python
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

operator_line = line[2].split(' ')[-2:]
self.operator_function = ops[operator_line[0]]
```


## Part 1
Just loop through each monkey keeping track of what goes where and how many items each monkey handles. Then put those values in a list, sort, and pull the two biggest out for multiplication.


## Part 2
I knew it was going to be tough when I saw a meme on reddit suggesting a math(s) degree was required. I looked for a hint which was not helpful and eventually worked it out myself.

The problem is that we want to do 10,000 rounds and with each round the values of the items (the worry level) gets bigger. One of the monkey's squares the value so there is exponential growth. The numbers get too big to store.

So - we have to make them smaller. However, we have to do so while making sure that the remainder will stay the same for the divisibility test. I wondered if I could factor the divisors but they're all prime. After a bit of guddling around I realised that:

```
    number % div = remainder
    number2 % div2 = remainder2

    number - (div * div2) = remainder
    number2 - (div * div2) = remainder2

```

If we calculate the product of all the divisors and subtract this from the value to be modulod then we'll get the same remainder if we modulo by one the divisors or the product.


Example
```
    divisors = 2, 3, 5
    factor = (2 * 3 * 5) = 30

    72 % 5 = 2
    (72 - 30) % 5 = 2
    (72 - 60) % 5 = 2
 
    72 % 3 = 0
    (72 - 30) % 3 = 0
    (72 - 60) % 3 = 0

```
So, in each round after making worry go up we then shrink it

```python
worry = worry - (((worry // factor) - 1) * factor)
```

We calculate how many times factor (the product of all the divisors) goes into worry and subtract that many multiples of factor less one. So, worry // factor = 1 and worry % divisor is the same before and after.
