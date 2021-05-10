""" exercise 208 Project Euler """
""" 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2**1000?
"""

x = 2**1000
y = str(x)
sum_of_digits = 0
for i in y:
    n = int(i)
    sum_of_digits += n

print("The sum of the digits: ", sum_of_digits)
