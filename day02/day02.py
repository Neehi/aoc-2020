import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  values = [(int(a), int(b), char, password) for line in file for a, b, char, password in [re.split(r'-|:? ', line.strip())]]

def part_one():
  return sum([password.count(char) in range(a, b + 1) for a, b, char, password in values])

def part_two():
  return sum([(password[a - 1] == char) != (password[b - 1] == char) for a, b, char, password in values])

if __name__ == "__main__":
  print('Part One: %d' % part_one())
  print('Part Two: %d' % part_two())
