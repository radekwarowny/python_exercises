''' exercise 195 Project Euler '''
''' What is the prime factor of the number 600851475143. '''


def prime_factor(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    print(int(n))


prime_factor(600851475143)