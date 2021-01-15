''' exercise 196 Project Euler '''
''' Find the largest palindrome made from the product of two 3-digit numbers. '''

products = []
a = []
b = []

for n in range(900, 999):
    a.append(n)
    b.append(n)

i = 900
while i < 1000:
    for x in a:
        product = x * i
        products.append(product)
    i += 1


for n in products:
    if str(n) == str(n)[::-1]:
        l_pal = n

print("Largest palindrome is: ", l_pal)










