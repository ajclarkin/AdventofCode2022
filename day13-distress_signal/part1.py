# Day 13 - Distress Signal

pairs = list(map(str.splitlines, open('input.txt').read().strip().split('\n\n')))

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
            # Here there's a problem with the input but not the example. We have deeper nesting of lists.
            # So, if we recurse into the function again it will handle it if the elements are ints but will loop deeper to unpack
            # if nests of lists.

            res = CompareLeftRight(left, right)
            if res == True or res == False:
                return res

            if len(left) < len(right):
                return True
            elif len(right) < len(left):
                return False
                
    if (len(l) < len(r)):
        return True



pair_count = 0
total = 0
for l, r in pairs:
    pair_count += 1
    res = CompareLeftRight(eval(l), eval(r))
    if res:
        total += pair_count
    print(res, l, r)

print(f"The total you're looking for is {total}")