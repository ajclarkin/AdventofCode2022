from collections import Counter

input = [x for x in open('input.txt').read().replace(' ', '').split('\n')]

# Now the second column is the outcome I need.
# X = lose, Y = draw, Z = win

combo = {
    'AX': (0 + 3),
    'AY': (3 + 1),
    'AZ': (6 + 2),
    'BX': (0 + 1),
    'BY': (3 + 2),
    'BZ': (6 + 3),
    'CX': (0 + 2),
    'CY': (3 + 3),
    'CZ': (6 + 1)
}

games = Counter(input)
points = 0

for k, v in combo.items():
    points += (games[k] * v)

print(f'Total points: {points}')