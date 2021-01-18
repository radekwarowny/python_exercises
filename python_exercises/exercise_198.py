''' exercise 198 Project Euler '''
''' Find the difference between the sum of the squares of
    the first one hundred natural numbers and the square of the sum. '''

x = 10
y = 100

def sum_of_squares(num):
    result = 0
    for i in range(1,num+1):
        n = i**2
        print(n, end=' ')
        result += n
    print("Result: ",result)
    return result

def square_of_sum(num):
    result = 0
    for i in range(1, num+1):
        result += i
    print("Result: ", result)
    result = result**2
    print("Square of the sum is: ", result)
    return result

a = sum_of_squares(x)
b = square_of_sum(x)

c = sum_of_squares(y)
d = square_of_sum(y)


print("First 10 natural numbers.")
print("Difference between the sum of the squares and square of the sum is: {} - {} = {}".format(b, a, (b-a)))
print("\nFirst 100 natural numbers.")
print("Difference between the sum of the squares and square of the sum is: {} - {} = {}".format(d, c, (d-c)))




