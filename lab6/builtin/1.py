from functools import reduce
from operator import mul

def multiply_numbers(numbers):
    result = reduce(mul, numbers, 1)
    return result
numbers_list = [2, 3, 4, 5]
result = multiply_numbers(numbers_list)
print(f"The product of the numbers in the list is: {result}")
