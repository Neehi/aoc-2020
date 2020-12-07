import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
    bags = {
      color: {c: n for n, c in re.findall('(\d+) (\w+ \w+) bag', contains)}
      for line in file
      for color, contains in (line.split(' bags contain '), )
      if contains != 'No other bags'
    }

def bags_containing(color):
  outer = {k for k, v in bags.items() if color in v}
  return outer.union(*[bags_containing(x) for x in outer])

def number_of_bags_inside(color):
  return sum([(1 + number_of_bags_inside(c)) * int(n) for c, n in bags[color].items()])

print('Part One: %d' % len(bags_containing('shiny gold')))
print('Part Two: %d' % number_of_bags_inside('shiny gold'))
