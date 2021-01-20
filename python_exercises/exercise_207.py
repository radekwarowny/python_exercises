""" exercise 207 Project Euler """
""" Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
    there are exactly 6 routes to the bottom right corner. 
    How many such routes are there through a 20×20 grid? """

# 1 X 1 grid = 2
# 2 X 2 grid = (2+1)*2 = 6

import math

def find_path(n):
    n_fac = math.factorial(n)
    result = math.factorial(2*n) / n_fac / n_fac
    return result

print(find_path(1))
print(find_path(2))
print(find_path(3))
print(find_path(4))
print(find_path(5))
print(find_path(20))





