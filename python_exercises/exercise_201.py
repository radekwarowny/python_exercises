""" exercise 201 Project Euler """
""" There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """

import math

def find_product():

    n = 1
    m = 1

    while n < 10:
        a = n

        while m <= 10:
            b = m
            c = (b**2) + (a**2)
            if (a**2) + (b**2) == c:
                if c % 2 != 0:
                    if (a%2==0) or (b%2==0):
                        if a < b < c:
                            print("Found", a, b, c)

            m += 1
            if m == 10:
                m = 1
                break

        n += 1







def find_triplet(num):
    a = num
    b = num
    c = num

    n = 0
    perfects_count = len(num)
    while n < perfects_count:
        for i in a:
            product = i + b[n] + c[n]
            #print(i, b[n], c[n], " = ", product)
            if i + b[n] + c[n] == 25:
                print("Found")


        n += 1



find_product()
#find_triplet(triplets)