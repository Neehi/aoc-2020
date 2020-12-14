import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

def run(use_memory_decoder=False):
  mem = {}
  for line in lines:
    if 'mask' in line:
      mask = line[7:]
    else:
      addr, value = map(int, re.findall(r'\d+', line))
      if not use_memory_decoder:
        mem[addr] = value & int(mask.replace('X', '1'), 2) | int(mask.replace('X', '0'), 2)
      else:
        for floating in map(iter, [bin(x)[2:].zfill(mask.count('X')) for x in range(2 ** mask.count('X'))]):
          x = ''.join(a if m == '0' else '1' if m == '1' else next(floating) for m, a in zip(mask, bin(addr)[2:].zfill(36)))
          mem[x] = value
  return sum(mem.values())

print('Part One: %d' % run())
print('Part Two: %d' % run(use_memory_decoder=True))
