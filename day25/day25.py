import os
from itertools import count

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  card_public_key, door_public_key = [int(line.strip()) for line in file]

def perform_iteration(value, subject_number):
  return (value * subject_number) % 20201227

n = 1
for card_loop_size in count(start=1):
  n = perform_iteration(n, 7)
  if n == card_public_key:
    break

encryption_key = 1
for _ in range(card_loop_size):
  encryption_key = perform_iteration(encryption_key, door_public_key)

print('Part One: %d' % encryption_key)
