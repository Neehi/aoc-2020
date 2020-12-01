import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as file:
  numbers = [int(line.strip()) for line in file]

def find_product_of_two(num, arr):
  for x in arr:
    compl = num - x
    if compl in arr[1:]:
      return x * compl

def find_product_of_three(num, arr):
  for i in range(len(arr) - 2):
    x = numbers[i]
    compl_x = num - x
    sum_yz = find_product_of_two(compl_x, numbers[i+1:])
    if sum_yz is not None:
      return x * sum_yz

if __name__ == "__main__":
  print('Part One: %d' % find_product_of_two(2020, numbers))
  print('Part Two: %d' % find_product_of_three(2020, numbers))
