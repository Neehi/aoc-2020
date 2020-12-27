cups = [int(c) for c in '327465189']

def play_cups(cups, moves):
  # Use a pseudo linked list to track cup positions
  arr = [0] * (len(cups) + 1)
  for i, x in enumerate(cups[:-1]):
    arr[x] = cups[i+1]
  arr[0] = arr[-1] = cups[0]

  current = arr[0]
  for _ in range(moves):
    a = arr[current]
    b = arr[a]
    c = arr[b]
    d = (current - 2) % len(cups) + 1
    while d in (a, b, c):
      d = (d - 2) % len(cups) + 1
    # From: current -> a -> b -> c -> c.next ... d -> d.next
    #   To: current -> c.next ... d -> a -> b -> c -> d.next
    arr[current], arr[c], arr[d] = arr[c], arr[d], a
    current = arr[current]

  # FIXME: Unnecessary overhead?
  final_state = []
  n = arr[1]
  while n != 1:
    final_state.append(n)
    n = arr[n]

  return final_state

# Part 1

p1 = play_cups(cups, 100)
print('Part One: %s' % ''.join(map(str, p1)))

# Part 2

p2 = play_cups(cups + list(range(max(cups)+1, 10**6+1)), 10**7)
print('Part Two: %d' % (p2[0] * p2[1]))
