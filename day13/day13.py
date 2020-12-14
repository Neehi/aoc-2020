import fractions  # import math if 3.5+
import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  notes = [line.strip() for line in file]
  earliest = int(notes[0])
  buses = {i: int(x) for i, x in enumerate(notes[1].split(',')) if x != 'x'}

def part_one():
  return reduce(lambda a, b: a * b, min({x: x - earliest % x for x in buses.values() if x != 'x'}.items(), key=lambda x: x[1]))

def part_two(initial_timestamp=0):
  """
  - Set step to first bus id
  - Find common timestep between first two buses
  - Next step is LCM of current step and bus id
  - Repeat for successive buses
  """
  step = buses.values()[0]
  ts = (initial_timestamp // step) * step if initial_timestamp else 0
  for i, bus in buses.items()[1:]:
    while (ts + i) % bus != 0:
      ts += step
    # All primes - use commented version if any non-prime
    # step = (step * bus) // fractions.gcd(step, bus)
    step *= bus
  return ts

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two(100000000000000L))
