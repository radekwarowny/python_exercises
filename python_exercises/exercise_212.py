""" exercise 212 Project Euler """
""" 
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""

start_number = 100
fac = 1

for i in range(start_number, 0, -1):
    fac *= i

fac_sum = 0
str_fac = str(fac)

for n in str_fac:
    digit = int(n)
    fac_sum += digit

print("Factorial: ", fac)
print("Sum of digits: ", fac_sum)


