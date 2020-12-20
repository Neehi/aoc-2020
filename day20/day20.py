import os
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
    self.data = [row for row in zip(*self.data[::-1])]

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
  grid[pos] = tile

  for id_2, tile_2 in tiles.items():
    if id_2 == tile.id: continue
    if tile_2 in grid.values(): continue

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

# Part 1

part_one = reduce(lambda a, b: a * b, [grid[j][i].id for j in (0,-1) for i in (0,-1)])
print('Part One: %d' % part_one)
