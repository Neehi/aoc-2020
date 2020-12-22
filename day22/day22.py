import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  decks = [line.strip() if line != '\n' else '\n' for line in file]

deck_1, deck_2 = [[int(x) for x in deck.strip().split('\n')[1:]] for deck in '\n'.join(decks).split('\n\n')]

def play_game(deck_1, deck_2, recursive=False):
  previous_decks = []

  while len(deck_1) and len(deck_2):
    if recursive and (deck_1, deck_2) in previous_decks:
      return 1
    previous_decks.append((deck_1[:], deck_2[:]))

    a, b = deck_1.pop(0), deck_2.pop(0)

    if recursive and a <= len(deck_1) and b <= len(deck_2):
      winner = play_game(deck_1[:a], deck_2[:b], recursive=True)
    else:
      winner = 1 if a > b else 2

    if winner == 1:
      deck_1.extend([a, b])
    else:
      deck_2.extend([b, a])

  return 1 if len(deck_1) else 2
 
def play(deck_1, deck_2, recursive=False):
  deck_1, deck_2 = deck_1[:], deck_2[:]
  winner = play_game(deck_1, deck_2, recursive=recursive)
  print(winner, deck_1, deck_2)
  return sum([x * (i + 1) for i, x in enumerate(reversed(deck_1 if winner == 1 else deck_2))])

print('Part One: %d' % play(deck_1, deck_2))
print('Part Two: %d' % play(deck_1, deck_2, recursive=True))
