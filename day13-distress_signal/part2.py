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

        print(f'Compare {left} with {right}\t\t{type(left)} - {type(right)}')

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
                print('Return True - int comparison')
                return True
            elif right < left:
                print('Return False - int comparison')
                return False


        if type(left) == list and type(right) == list:
            print(f"Call function again {left} ---- {right}")
            res = CompareLeftRight(left, right)
            print(f"Nested function return {res}")
            if res == True or res == False:
                return res

            # for ll, rr in zip(left, right):
            #     if ll < rr:
            #         # print('Return True - int in list comparison')
            #         return True
            #     elif rr < ll:
            #         # print('Return False - int in list comparison')
            #         return False

            if len(left) < len(right):
                # print('Return True - list length comparison')
                return True
            elif len(right) < len(left):
                # print('Return False - list length comparison')
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