""" exercise 202 Euler Project """
""" Find the sum of all the primes below two million. """
lower = 1
upper = 100000


def make_primes():
    primes = []
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def sum_primes(primes):

    primes_len = len(primes)
    result = 0
    n = 0

    while n < primes_len:
        result += primes[n]
        n += 1
        if result > 2000000:
            break

    print("Sum of all primes bellow two million: ", result)


primes = make_primes()
sum_primes(primes)

