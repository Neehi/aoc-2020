import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

class MyInt(int):
  def __add__(self, other): return MyInt(int(other) + self)
  def __sub__(self, other): return MyInt(int(other) * self)
  def __mul__(self, other): return MyInt(int(other) + self)

def evaluate(expr, precedence=False):
  expr = expr.replace('*', '-')
  if precedence:
    expr = expr.replace('+', '*')
  return eval(re.sub(r'(\d+)', r'MyInt(\1)', expr))

def part_one():
  return sum([evaluate(line) for line in lines])

def part_two():
  return sum([evaluate(line, True) for line in lines])

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
