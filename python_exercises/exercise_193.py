''' exercise 193 Project Euler '''

''' Find the sum of all the multiples of 3 and 5 below 1000.'''


def find_multiples(num):
    multiples = []
    for n in range(1, num):
        if n % 3 == 0:
            multiples.append(n)
        elif n % 5 == 10:
            multiples.append(n)
        else:
            pass
    print(multiples)


find_multiples(10)
find_multiples(1000)
