import os
from operator import or_

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  answers = [
    [set(x) for x in group.split()]
    for group in ' '.join([line.strip() if line != '\n' else line for line in file]).split(' \n')
  ]

part_one = sum([len(reduce(or_, group)) for group in answers])
part_two = sum([len(set.intersection(*group)) for group in answers])

print('Part One: %d' % part_one)
print('Part Two: %d' % part_two)
