from collections import OrderedDict

cups = [int(c) for c in '327465189']

def play_cups(cups, moves):
  # Use a pseudo linked list to track cup positions
  cups = OrderedDict((a, b) for a, b in zip(cups, cups[1:] + cups[:1]))

  current = next(iter(cups))
  for _ in range(moves):
    a = cups[current]
    b = cups[a]
    c = cups[b]
    d = (current - 2) % len(cups) + 1
    while d in (a, b, c):
      d = (d - 2) % len(cups) + 1
    # current -> c.next
    # d -> a -> b -> c -> d.next
    cups[current] = cups[c]
    cups[c] = cups[d]
    cups[d] = a
    current = cups[current]

  # FIXME: Unnecessary overhead :/
  final_state = []
  n = cups[1]
  while n != 1:
    final_state.append(n)
    n = cups[n]

  return final_state

print('Part One: %s' % ''.join([str(x) for x in play_cups(cups, 100)]))
