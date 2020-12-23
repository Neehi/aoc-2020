cups = [int(c) for c in '327465189']

def play_cups(cups, moves):
  cups = cups[:]
  for _ in range(moves):
    current = cups[0]
    picked_up = cups[1:4]
    destination = max(cups[4:]) if current < min(cups[4:]) else max([x for x in cups[4:] if x < current])
    i = cups.index(destination)
    cups = cups[4:i+1] + picked_up + cups[i+1:] + [current]
  return cups[cups.index(1)+1:] + cups[:cups.index(1)]

print('Part One: %s' % ''.join([str(x) for x in play_cups(cups, 100)]))
