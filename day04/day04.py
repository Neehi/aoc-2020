import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  passports = [
    {k: v for parts in (passport.split(), ) for part in parts for k, v in (part.split(':'), )}
    for passport in ' '.join([line.strip() if line != '\n' else line for line in file]).split(' \n')
  ]

def check_required_fields(passport):
  return all(k in passport for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))

def check_valid_values(passport):
  return (
    1920 <= int(passport['byr']) <= 2002 and
    2010 <= int(passport['iyr']) <= 2020 and
    2020 <= int(passport['eyr']) <= 2030 and
    (passport['hgt'][3:] == 'cm' and 150 <= int(passport['hgt'][:3]) <= 193 or
     passport['hgt'][2:] =='in' and 59 <= int(passport['hgt'][:2]) <= 76) and
    len(passport['hcl']) == 7 and passport['hcl'][0] == '#' and all(ch in '0123456789abcdef' for ch in passport['hcl'][1:]) and
    passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
    len(passport['pid']) == 9 and all(ch in '0123456789' for ch in passport['pid'])
  )

def part_one():
  return sum([check_required_fields(passport) for passport in passports])

def part_two():
  return sum([check_valid_values(passport) for passport in passports if check_required_fields(passport)])

print('Part One: %d' % part_one())
print('Part Two: %d' % part_two())
