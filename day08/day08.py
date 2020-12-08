import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  instructions = [(op, int(val)) for line in file for op, val in (line.strip().split(), )]

def run(program):
  visited = set()
  pc = acc = 0
  while pc < len(program) and pc not in visited:
    visited.add(pc)
    op, val = program[pc]
    if op == 'jmp':
      pc += val
      continue
    if op == 'acc':
      acc += val
    pc += 1
  return pc, acc

def part_one():
  return run(instructions)[1]

def part_two():
  for i in range(len(instructions)):
    op, val = instructions[i]
    if op != 'acc':
      instructions[i] = ('nop', val) if op == 'jmp' else ('jmp', val)
      pc, acc = run(instructions)
      instructions[i] = (op, val)
      if pc >= len(instructions):
        return acc

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
