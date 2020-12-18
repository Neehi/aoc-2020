import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

def evaluate(expr, precedence=False):
  if precedence:
    # Part 2: Split expr by '*' -> evaluate parts -> mul parts
    expr = ' * '.join([str(evaluate(part, False)) for part in expr.split(' * ')])
  parts = expr.split()
  lhs = int(parts.pop(0))
  while len(parts):
    op, rhs = parts.pop(0), int(parts.pop(0))
    lhs = lhs + rhs if op == '+' else lhs * rhs
  return lhs

def solve(expr, precedence=False):
  # Solve expression by recursively evaluating
  # expressions between parenthesis
  i = expr.rfind('(')
  if i != -1:
    j = expr.find(')', i)
    expr = expr[:i] + str(evaluate(expr[i+1:j], precedence)) + expr[j+1:]
    return solve(expr, precedence)
  return evaluate(expr, precedence)

def part_one():
  return sum([solve(line) for line in lines])

def part_two():
  return sum([solve(line, precedence=True) for line in lines])

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
