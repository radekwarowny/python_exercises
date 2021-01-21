""" exercise 210 Project Euler """
# description https://projecteuler.net/problem=18

# Not finished!

t1 = [3]
t2 = [7, 4]
t3 = [2, 4, 6]
t4 = [8, 5, 9, 3]

triangle = [t1, t2, t3, t4]
values = []
max_value = []
result = 0
for i in triangle:
    print(i)
    for n in i:
        values.append(n)
    max_value.append(max(values))
    values = []
print(max_value)






