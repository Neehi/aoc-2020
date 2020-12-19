import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  lines = [line.strip() for line in file]

rules, messages = [[x.strip() for x in chunk.strip().split('\n')] for chunk in '\n'.join(lines).split('\n\n')]
rules = {int(k): v.replace('"', '') for rule in rules for k, v in (rule.split(': '), )}

def parse_rule(id):
  rule = rules[id]
  if rule == 'a' or rule == 'b':
    return rule
  return '(?:' + ''.join([x if x in '|+' or x.startswith('{') else parse_rule(int(x)) for x in rule.split()]) + ')'

def is_message_valid(message, rule):
  return re.match('^' + rule + '$', message) is not None

# Part 1

rule_0 = parse_rule(0)
part_one = sum([is_message_valid(message, rule_0) for message in messages])

print('Part One: %d' % part_one)

# Part 2

# Replace rules 8 and 11:
#   42 --> 42 | 42 8 --> 42 42 8... --> (42)+
#   42 31 --> 42 31 | 42 11 31 --> 42 42 11 31 31... --> (42){n}(31){n}
rules[8] = '42 +'
rules[11] = '42 {n} 31 {n}'

rule_0 = parse_rule(0)
part_two = sum([sum([is_message_valid(message, rule_0.replace('n', str(n))) for n in range(1, 6)]) for message in messages])

print('Part Two: %d' % part_two)
