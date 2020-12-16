import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  fields_input, your_ticket_input, nearby_tickets_input = [lines.split('\n')
                                                           for lines in file.read().strip().split('\n\n')]

fields = {
  field: [tuple(int(n) for n in x.split('-')) for x in ranges.split(' or ')]
  for line in fields_input for field, ranges in (line.split(': '), )
}
your_ticket = [int(x) for x in your_ticket_input[1].split(',')]
nearby_tickets = [[int(x) for x in line.split(',')] for line in nearby_tickets_input[1:]]

possible_fields = [set() for field in fields]
error_rate = 0

for ticket in nearby_tickets:
  valid_fields = []
  for i, x in enumerate(ticket):
    matching_fields = [j for j, field in enumerate(fields.values()) if any(m <= x <= n for m, n in field)]
    if matching_fields:
      valid_fields.append(matching_fields)
    else:
      error_rate += x
  if len(valid_fields) == len(fields):
    for i, x in enumerate(valid_fields):
      possible_fields[i] = possible_fields[i].intersection(x) if possible_fields[i] else set(x)

print('Part One: %d' % error_rate)

while any(len(s) > 1 for s in possible_fields):
  possible_fields = [
    s if len(s) == 1 else s ^ s.intersection([next(iter(x)) for x in possible_fields if len(x) == 1])
    for s in possible_fields
  ]
matched_fields = [next(iter(s)) for s in possible_fields]

departure_hash = reduce(
  lambda a, b: a * b,
  [your_ticket[i] for i, x in enumerate(matched_fields) if fields.keys()[x].startswith('departure')]
)

print('Part Two: %d' % departure_hash)
