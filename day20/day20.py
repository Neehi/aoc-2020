import os
import re
from collections import OrderedDict

directions = 'NESW'
deltas = [(-1,0), (0,+1), (+1,0), (0,-1)]  # (dy,dx)

class Tile:
  
  def __init__(self, id, data):
    self.id = id
    self.data = [list(row) for row in data]

  def side(self, dir):
    if dir == 'N':
      return self.data[0]
    elif dir == 'S':
      return self.data[-1]
    elif dir == 'E':
      return [row[-1] for row in self.data]
    elif dir == 'W':
      return [row[0] for row in self.data]

  def find_matching_edge(self, other):
    return next((d for d in directions if self.side(d) == other.side('SWNE'[directions.index(d)])), None)

  def rot_90(self):
    self.data = [''.join(row) for row in zip(*self.data[::-1])]

  def flip_h(self):
    self.data = [row[::-1] for row in self.data]

# Build grid

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

tiles = {int(chunk[5:9]): Tile(int(chunk[5:9]), chunk.split('\n')[1:]) for chunk in '\n'.join(lines).split('\n\n')}

grid = dict()
queue = [((0, 0), tiles.values()[0])]

while len(queue):
  pos, tile = queue.pop(0)

  if pos in grid: continue
  grid[pos] = tile.id

  for id_2, tile_2 in tiles.items():
    if id_2 == tile.id or id_2 in grid.values(): continue

    for _ in range(2):
      for _ in range(4):
        matching_edge = tile.find_matching_edge(tile_2)
        if matching_edge:
          pos_2 = tuple(x + dx for x, dx in zip(pos, deltas[directions.index(matching_edge)]))
          queue.append((pos_2, tile_2))
          break
        tile_2.rot_90()
      else:
        tile_2.flip_h()
        continue
      break

grid = OrderedDict(sorted(grid.items(), key=lambda t: t[0]))

grid_size = int(len(tiles) ** 0.5)
grid = [grid.values()[j:j+grid_size] for j in range(0, len(grid), grid_size)]

tile_size = len(tiles.values()[0].data)

# Part 1

part_one = reduce(lambda a, b: a * b, [grid[j][i] for j in (0,-1) for i in (0,-1)])
print('Part One: %d' % part_one)

# Part 2

image = [
  ''.join([''.join(tiles[grid[k][i]].data[j][1:-1]) for i in range(grid_size)])
  for k in range(grid_size) for j in range(1, tile_size-1)
]

monster_patterns = [r'.{18}#.', r'#.{4}##.{4}##.{4}###', r'.#..#..#..#..#..#...']
monster_roughness = sum([x.count('#') for x in monster_patterns])
roughness = ''.join(image).count('#')

image_size = len(image) + 1

for _ in (False, True):
  for _ in range(4):
    image_str = '\n'.join(image)
    monsters = sum([
      all(
        re.match(monster_patterns[x], image_str[match.start(0)+offset:match.start(0)+offset+20])
        for x, offset in ((0, -image_size), (2, image_size))
      )
      for match in re.finditer(monster_patterns[1], image_str[:-2])
    ])
    if monsters > 0:
      break
    image = [''.join(row) for row in zip(*image[::-1])]
  else:
    image = [''.join(row[::-1]) for row in image]
    continue
  break

print('Part Two: %d' % (roughness - (monsters * monster_roughness)))
