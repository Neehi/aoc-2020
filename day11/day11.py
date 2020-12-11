import os
from copy import deepcopy

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  seats = [list(line.strip()) for line in file]

NUM_ROWS = len(seats)
NUM_COLS = len(seats[0])

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

neighbours = [
  (-1, -1), ( 0, -1), (+1, -1),
  (-1,  0),           (+1,  0),
  (-1, +1), ( 0, +1), (+1, +1),
]

def get_neighbours(x, y, adjacent_only=True):
  return list(filter(None, [
    next((
      (x + i * step, y + j * step) for step in range(1, 2 if adjacent_only else max(NUM_ROWS, NUM_COLS))
      if 0 <= (x + i * step) < NUM_COLS and 0 <= (y + j * step) < NUM_ROWS and seats[y + j * step][x + i * step] != FLOOR
    ), None) for i, j in neighbours
  ]))

def process_seating(adjacent_only, tolerance):
  curr_plan, next_plan = [], deepcopy(seats)
  while curr_plan != next_plan:
    curr_plan = deepcopy(next_plan)
    for y, row in enumerate(curr_plan):
      for x, seat in enumerate(row):
        if seat == EMPTY and all([curr_plan[j][i] != OCCUPIED for i, j in get_neighbours(x, y, adjacent_only)]):
          next_plan[y][x] = OCCUPIED
        elif seat == OCCUPIED and sum([curr_plan[j][i] == OCCUPIED for i, j in get_neighbours(x, y, adjacent_only)]) >= tolerance:
          next_plan[y][x] = EMPTY
  return sum([row.count(OCCUPIED) for row in next_plan])

print('Part One: %d' % process_seating(True, 4))
print('Part Two: %d' % process_seating(False, 5))
