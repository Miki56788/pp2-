from functools import reduce
from operator import mul
import time
import math
def multiply_list(numbers):
    return reduce(mul, numbers)


numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))
