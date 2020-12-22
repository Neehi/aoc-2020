import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  decks = [line.strip() if line != '\n' else '\n' for line in file]

deck_1, deck_2 = [[int(x) for x in deck.strip().split('\n')[1:]] for deck in '\n'.join(decks).split('\n\n')]

def score(deck):
  return sum([(len(deck) - i) * x for i, x in enumerate(deck)])

def play_game(deck_1, deck_2, recursive=False):
  deck_1, deck_2 = deck_1[:], deck_2[:]
  previous_decks = []

  while len(deck_1) and len(deck_2):
    if recursive and (deck_1, deck_2) in previous_decks:
      return 1, 0

    previous_decks.append((deck_1[:], deck_2[:]))

    a, b = deck_1.pop(0), deck_2.pop(0)

    if recursive and a <= len(deck_1) and b <= len(deck_2):
      p1_wins = play_game(deck_1[:a], deck_2[:b], recursive=True)[0] > 0
    else:
      p1_wins = a > b

    if p1_wins:
      deck_1.extend([a, b])
    else:
      deck_2.extend([b, a])

  return score(deck_1), score(deck_2)
 
print('Part One: %d' % max(play_game(deck_1, deck_2)))
print('Part Two: %d' % max(play_game(deck_1, deck_2, recursive=True)))
