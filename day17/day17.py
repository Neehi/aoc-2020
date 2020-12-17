import os
from itertools import product

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

# As it's infinite space and only 2 states, just keep track of actives
grid = {(i, j, 0) for j, row in enumerate(lines) for i, cube in enumerate(row) if cube == '#'}

deltas = [delta for delta in product((-1, 0, 1), repeat=3) if delta != (0, 0, 0)]

def process_grid(grid, cycles):
  for cycle in range(cycles):
    # Keep track of neighbours to actives:
    #   {(x,y,z): n} where n = number of actives around that neighbour
    neighbours = dict()
    for cube in grid:
      for delta in deltas:
        neighbour = tuple(c + d for c, d in zip(cube, delta))
        neighbours[neighbour] = neighbours[neighbour] + 1 if neighbour in neighbours else 1
    # Re-build the grid based on number of actives around each identified neighbour
    grid = {
      cube for cube, n in neighbours.items()
      if (cube in grid and n in (2, 3))  # An active with 2-3 neighbours
      or (cube not in grid and n == 3)   # An inactive with 3 neighbours
    }
  return len(grid)

print('Part One: %d' % process_grid(grid, 6))
