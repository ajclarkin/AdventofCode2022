# Day 11 - Monkey in the Middle, part 1

import operator
from collections import deque
import math

input = [chunk for chunk in open('input.txt').read().split('\n\n')]
monkeys = []

'''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
'''


class Monkey:

    def __init__(self, chunk):
        # parse the chunk into what we need
        line = [l for l in chunk.split('\n')]
        self.total_items = 0

        # Line 1
        self.items = [int(x) for x in line[1].split(':')[1].strip().split(',')]

        # Line 2
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        operator_line = line[2].split(' ')[-2:]
        self.operator_function = ops[operator_line[0]]
        self.operator_value = None if operator_line[1] == 'old' else int(operator_line[1])

        # Line 3
        self.test = int(line[3].split(' ')[-1])

        # Line 4
        self.monkey_true = line[4].split(' ')[-1]
        self.monkey_false = line[5].split(' ')[-1]


    def GetItems(self):
        self.total_items += len(self.items)
        return self.items


    def ClearItemList(self):
        self.items.clear()


    def CatchItem(self, item):
        self.items.append(item)



# Populate the objects
for i in input:
    monkeys.append(Monkey(i))

for rounds in range(20):
    # One round:
    for m in monkeys:
        # for item in monkeys[m].GetItems():
        for item in m.GetItems():
            val = item if m.operator_value == None else m.operator_value
            worry = m.operator_function(val, item)
            worry = worry // 3

            new_monkey = m.monkey_true if (worry % m.test == 0) else m.monkey_false
            monkeys[int(new_monkey)].CatchItem(worry)
        m.ClearItemList()



# Now find the two monkeys with most objects and find the product of each no
totals = []
for m in monkeys:
    totals.append(m.total_items)

final = math.prod(sorted(totals, reverse=True)[:2])
print(f'THe final value of monkey business is {final}')