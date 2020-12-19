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
  return '(?:' + ''.join([parse_rule(int(x)) if x != '|' else x for x in rule.split()]) + ')'

def part_one():
  rule_0 = re.compile('^' + parse_rule(0) + '$')
  return sum([re.match(rule_0, message) is not None for message in messages])

print('Part One: %d' % part_one())
