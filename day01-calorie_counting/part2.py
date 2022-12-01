# day01 - Calorie Counting
# Part 2 - find the 3 largest items in sum_list

input = [x for x in open('input.txt').read().split('\n')]

sum_v = 0
sum_list = []

for x in input:
    if x == '':
        sum_list.append(sum_v)
        sum_v = 0
    else:
        sum_v += int(x)


sum_list.sort(reverse=True)
print(sum(sum_list[0:3]))



