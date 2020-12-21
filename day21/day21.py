import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  foods = [line.strip() for line in file]

foods = [
  (ingredients.split(), allergens[:-1].split(', '))
  for food in foods for ingredients, allergens in (food.split(' (contains '), )
]

ingredients = dict()  # List of ingredient with how many times they appear
allergens = dict()  # List of allergens with ingredients

for ingredients_, allergens_ in foods:
  for ingredient_ in ingredients_:
    ingredients[ingredient_] = ingredients[ingredient_] + 1 if ingredient_ in ingredients else 1
  for allergen_ in allergens_:
    # Intersection of all ingredients across all foods containing that allergen
    allergens[allergen_] = set.intersection(*[set(x) for x, a in foods if allergen_ in a])

# Part 1

cant_contain_allergens = set(ingredients) - set.union(*allergens.values())

part_one = sum([v for k, v in ingredients.items() if k in cant_contain_allergens])
print('Part One: %d' % part_one)

# Part 2

# Narrow the allergens down to a single ingredient per allergen
while any(len(s) > 1 for s in allergens.values()):
  for k, s in allergens.items():
    if len(s) > 1:
      allergens[k] ^= s.intersection([next(iter(x)) for x in allergens.values() if len(x) == 1])

dangerous_ingredients = [next(iter(x)) for _, x in sorted(allergens.items(), key=lambda t: t[0])]

print('Part Two: %s' % ','.join(dangerous_ingredients))
