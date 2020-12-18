import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

class MyInt(int):
  def __add__(self, other): return MyInt(int(other) + self)
  def __sub__(self, other): return MyInt(int(other) * self)
  def __mul__(self, other): return MyInt(int(other) + self)

def evaluate(expr, repl):
  expr = ''.join([c if c not in '+*' else next(v for k, v in repl.items() if k == c) if c in repl else c for c in expr])

  elems = []
  prev = ''
  for c in expr:
    if c.isdigit() and not prev.isdigit():
      elems.append('MyInt(')
    elif not c.isdigit() and prev.isdigit():
      elems.append(')')
    elems.append(c)
    prev = c
  if elems[-1].isdigit():
    elems.append(')')

  return eval(''.join(elems))

def part_one():
  return sum([evaluate(line, {'*': '-'}) for line in lines])

def part_two():
  return sum([evaluate(line, {'*': '-', '+': '*'}) for line in lines])

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
