import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  adapters = sorted([int(line.strip()) for line in file])

def part_one():
  jolts, d_1, d_3 = 0, 0, 1
  for x in adapters:
    diff = x - jolts
    d_1 += diff == 1
    d_3 += diff == 3
    jolts = x
  return d_1 * d_3

def part_two():
  diffs = [str(adapters[i] - x) for i, x in enumerate([0] + adapters[:-1])]
  runs = [len(x) for x in ''.join(diffs).split('3') if len(x) > 1]
  return reduce(lambda a, b: a * (7 if b == 4 else 4 if b == 3 else b), [1] + runs)

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
