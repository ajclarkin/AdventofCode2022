# Day 13 - Distress Signal, part 2

lines = [x for x in open('input.txt').read().split('\n')]
while lines.count(''):
    lines.remove('')


items = [eval(l) for l in lines]
items.append([[2]])
items.append([[6]])


def CompareLeftRight(l, r):
    for k, left in enumerate(l):

        if len(r) == k:
            # Got to end of item and left is longer than right
            # eg if k = 3 then we're looking for item 4 (zero-index) and so if len = 3 we have a problem
            # print('Oh dear, end of the road')
            return False
        else:
            right = r[k]


        if type(left) == int and type(right) == list:
            temp = left
            left = list()
            left.append(temp)

        if type(right) == int and type(left) == list:
            temp = right
            right = list()
            right.append(temp)

        if type(left) == int and type(right) == int:
            if left < right:
                return True
            elif right < left:
                return False


        if type(left) == list and type(right) == list:
            res = CompareLeftRight(left, right)
            if res == True or res == False:
                return res

            if len(left) < len(right):
                return True
            elif len(right) < len(left):
                return False
    if (len(l) < len(r)):
        return True





made_change = True

while made_change == True:
    made_change = False
    for k, v in enumerate(items):
        if k+1 < len(items):
            if not CompareLeftRight(v, items[k+1]):
                temp = items.pop(k)
                items.insert(k+1, temp)
                made_change = True

pos1 = items.index([[2]]) + 1
pos2 = items.index([[6]]) + 1

print(f"The decoder key is {pos1 * pos2}")