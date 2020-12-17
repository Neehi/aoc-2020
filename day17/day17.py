import os
from itertools import product

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

# As it's infinite space and only 2 states, just keep track of actives
initial_grid = {(i, j) for j, row in enumerate(lines) for i, cube in enumerate(row) if cube == '#'}

def process_grid(initial_grid, dimensions, cycles):
  # Setup grid and deltas based on number of dimensions
  grid = {cube + (0, ) * (dimensions - 2) for cube in initial_grid}
  deltas = [delta for delta in product((-1, 0, 1), repeat=dimensions) if delta != (0, ) * dimensions]

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

print('Part One: %d' % process_grid(initial_grid, 3, 6))
print('Part Two: %d' % process_grid(initial_grid, 4, 6))
