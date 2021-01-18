""" exercise 203 Project Euler """
""" What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid?"""

def triangle_no_seq():
    n = 0
    seq = []
    for i in range(10):
        n += i
        seq.append(n)
    return seq



def find_divisors(nums):
    i = 1
    o = 0
    print("Sequence: ", nums)
    foo = len(nums)

    for n in nums:
        while n % 1
        if n % i == 0:
            print(n, i)
        i += 1




sequence = triangle_no_seq()
print()
find_divisors(sequence)

