from collections import Counter

input = [x for x in open('input.txt').read().replace(' ', '').split('\n')]

# Combos are opponent and me
# Lose = 0, draw = 3, win = 6 PLUS X = 1, Y = 2, Z = 3

combo = {
    'AX': (3 + 1),
    'AY': (6 + 2),
    'AZ': (0 + 3),
    'BX': (0 + 1),
    'BY': (3 + 2),
    'BZ': (6 + 3),
    'CX': (6 + 1),
    'CY': (0 + 2),
    'CZ': (3 + 3)
}

games = Counter(input)
points = 0

for k, v in combo.items():
    points += (games[k] * v)

print(f'Total points: {points}')