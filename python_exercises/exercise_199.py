''' exercise 199 Project Euler '''

''' 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
 '''


def find_if_prime(num):
    a = 2
    while num > a:
        if num % a == 0 and a != num:
            #print("not prime")
            break
        a += 1
    else:
        return num


def find_nth_prime(n):
    count = 1
    primes = 0

    while primes < n:
        if find_if_prime(count):
            primes += 1
            result = find_if_prime(count)
        else:
            pass
        count += 1

    print("The {}th prime number is: {}".format(n, result))



find_nth_prime(50)
find_nth_prime(500)
find_nth_prime(5000)
# find_nth_prime(10001)  this will crash your pc

