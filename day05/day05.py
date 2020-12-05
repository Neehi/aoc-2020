import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  seats = [
    int(''.join(['1' if ch in ('R', 'B') else '0' for ch in line.strip()]), 2)
    for line in file
  ]

max_id = max(seats)
missing_id = set(range(min(seats), max_id)).difference(seats).pop()

print('Part One: %d' % max_id)
print('Part Two: %d' % missing_id)
