import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  tree_map = [line.strip() for line in file]

trees = [
  sum([row[(i * dx + 1) % len(tree_map[0]) - 1] == '#' for i, row in enumerate(tree_map) if dy == 1 or i % dy == 0])
  for dx, dy in [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]
]

print('Part One: %d' % trees[0])
print('Part Two: %d' % reduce(lambda x, y: x * y, trees))
