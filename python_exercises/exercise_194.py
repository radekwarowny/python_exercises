''' exercise 194 Project Euler '''
''' Find the sum of the even-valued terms in fibonacci sequence. '''
# Function argument is last fibonacci number.


def fibonacci(num):
    n1, n2 = 0, 1
    count = 0
    sequence = []

    if num <= 0:
        print("Input error.")
    elif num == 1:
        print("Fibonacci sequence: ", num)
    else:
        print("Fibonacci sequence: ")
        while count < num:
            print(n1)
            sequence.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
            if n1 > 4000000:
                break
    return sequence


def fibonacci_sum(n):

    num = 0
    for i in n:
        if i % 2 != 0:
            pass
        else:
            num += i
    print("Sum of fibonacci even-valued terms: ", num)


print(fibonacci(50))
fibonacci_sum(fibonacci(50))
