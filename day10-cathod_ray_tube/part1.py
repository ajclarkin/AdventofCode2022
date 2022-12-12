# Day 10 - Cathode Ray Tube, part 1

input = [line for line in open('input.txt').read().split('\n')]
cycle = 1
register = 1
total = 0

for row_no, row in enumerate(input):
    words = row.split()
    if (cycle % 40 == 20):
            total += (cycle * register)
    if (cycle % 40 == 21) and prev_command == 'addx' :
            total += ((cycle-1) * (register - prev_value))

    if words[0] == 'noop':
        cycle += 1
        prev_command = words[0]
    else:
        cycle += 2
        register += int(words[1])
        prev_value = int(words[1])
        prev_command = words[0]

        

print(f'Final total: {total}')