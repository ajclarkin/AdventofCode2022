# day01 - Calorie Counting

input = [x for x in open('input.txt').read().split('\n')]

sum = 0
sum_list = []

for x in input:
    if x == '':
        sum_list.append(sum)
        sum = 0
    else:
        sum += int(x)

print(f'The elf with the most calories has {max(sum_list)} calories')