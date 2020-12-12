import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  instructions = [(line[0], int(line.strip()[1:])) for line in file]

directions = 'NESW'

def part_one():
  d, x, y = 'E', 0, 0
  for action, value in instructions:
    if action in 'RL':
      d = directions[(directions.index(d) + (value if action == 'R' else -value) // 90) % 4]
      continue
    if action == 'F':
      action = d
    if action == 'E':
      x += value
    elif action == 'W':
      x -= value
    elif action == 'N':
      y += value
    elif action == 'S':
      y -= value
  return abs(x) + abs(y)

def part_two():
  wpx, wpy, x, y = 10, 1, 0, 0
  for action, value in instructions:
    if action in 'RL':
      for i in range(((value if action == 'R' else -value) // 90) % 4):
        wpx, wpy = wpy, -wpx
    elif action == 'E':
      wpx += value
    elif action == 'W':
      wpx -= value
    elif action == 'N':
      wpy += value
    elif action == 'S':
      wpy -= value
    elif action == 'F':
      x += wpx * value
      y += wpy * value
  return abs(x) + abs(y)

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
