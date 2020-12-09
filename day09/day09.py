import os
from itertools import combinations

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  numbers = [int(line.strip()) for line in file]

def invalid_number(preamble):
  return next(
    numbers[i] for i in range(preamble, len(numbers))
    if numbers[i] not in [sum(pair) for pair in combinations(numbers[i-preamble:i], 2)]
  )

def encryption_weakness(target):
  i, t = 0, numbers[0]
  for j in range(1, len(numbers)):
    t += numbers[j]
    while t > target:
      t -= numbers[i]
      i += 1
    if t == target:
      return min(numbers[i:j]) + max(numbers[i:j])

part_one = invalid_number(25)
part_two = encryption_weakness(part_one)

print('Part One: %d' % part_one)
print('Part Two: %d' % part_two)
