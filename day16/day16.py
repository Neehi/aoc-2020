import os
from operator import mul

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  fields_input, your_ticket_input, nearby_tickets_input = [lines.split('\n')
                                                           for lines in file.read().strip().split('\n\n')]

fields = {
  field: [tuple(int(n) for n in x.split('-')) for x in ranges.split(' or ')]
  for line in fields_input for field, ranges in (line.split(': '), )
}
your_ticket = [int(x) for x in your_ticket_input[1].split(',')]
nearby_tickets = [[int(x) for x in line.split(',')] for line in nearby_tickets_input[1:]]

errors = []
error_rate = 0
for i, ticket in enumerate(nearby_tickets):
  for x in ticket:
    if all(x not in range(m, n + 1) for ranges in fields.values() for m, n in ranges):
      errors.append(i)
      error_rate += x

print('Part One: %d' % error_rate)

possible_fields = [set() for field in fields]
for i, ticket in enumerate(nearby_tickets):
  if i not in errors:
    for j, x in enumerate(ticket):
      possibles = [k for k, ranges in enumerate(fields.values()) if any(m <= x <= n for m, n in ranges)]
      possible_fields[j] = possible_fields[j].intersection(possibles) if possible_fields[j] else set(possibles)

while any(len(s) > 1 for s in possible_fields):
  for i, s in enumerate(possible_fields):
    if len(s) > 1:
      possible_fields[i] ^= s.intersection([next(iter(x)) for x in possible_fields if len(x) == 1])
matched_fields = [next(iter(s)) for s in possible_fields]

departure_hash = reduce(mul, [n for x, n in zip(matched_fields, your_ticket) if fields.keys()[x].startswith('departure')])

print('Part Two: %d' % departure_hash)
