import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  adapters = sorted([int(line.strip()) for line in file])

def part_one():
  diffs = [b - a for a, b in zip([0] + adapters[:-1], adapters)]
  return diffs.count(1) * (diffs.count(3) + 1)

def part_two():
  paths = {0: 1}
  for x in adapters:
    paths[x] = sum([paths.get(i, 0) for i in range(x-3, x)])
  return paths[x]

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
