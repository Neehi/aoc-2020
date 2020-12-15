numbers = [12, 20, 0, 6, 1, 17, 7]

def find_last_spoken(rounds):
  # Last time spoken was last turn, and
  # previous time spoken is stored in spoken[last]
  spoken = {x: i for i, x in enumerate(numbers)}
  last = input[-1]
  for x in range(len(input), rounds):
    n = (x - 1) - spoken[last] if last in spoken else 0
    spoken[last] = x - 1
    last = n
  return n

print('Part One: %d' % find_last_spoken(2020))
print('Part Two: %d' % find_last_spoken(30000000))
