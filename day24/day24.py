import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  instructions = [line.strip() for line in file]

# Rows rotated 45 deg:
#         _____
#   _____/ 0,1 \_____
#  /-1,1 \_____/ 1,0 \
#  \_____/ 0,0 \_____/
#  /-1,0 \_____/ 1,-1\
#  \_____/ 0,-1 \____/
#        \_____/

directions = {
  'w': (-1, 0), 'nw': (-1, +1), 'ne': (0, +1),
  'e': (+1, 0), 'se': (+1, -1), 'sw': (0, -1), 
}

black_tiles = set()

# Part 1

for steps in instructions:
  tile = (0, 0)
  for d in [match.group(0) for match in re.finditer(r'e|se|sw|w|nw|ne', steps)]:
    tile = tuple([tx + dx for tx, dx in zip(tile, directions[d])])
  if tile in black_tiles:
    black_tiles.remove(tile)
  else:
    black_tiles.add(tile)

print('Part One: %d' % len(black_tiles))

# Part 2

for _ in range(100):
  # Keep track of neighbours to black tiles:
  #   {(x,y): n} where n = number of black tiles around that neighbour
  neighbours = dict()
  for tile in black_tiles:
    for delta in directions.values():
      neighbour = tuple(tx + dx for tx, dx in zip(tile, delta))
      neighbours[neighbour] = neighbours[neighbour] + 1 if neighbour in neighbours else 1

  # Re-build the grid based on number of black tiles around each identified neighbour
  black_tiles = {tile for tile, n in neighbours.items() if n == 2 or (n == 1 and tile in black_tiles)}

print('Part 2: % d' % len(black_tiles))
