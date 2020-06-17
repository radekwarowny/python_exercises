import random

x = random.randint(0, 10)

print("My random number is ", x)
print("Here are som numbers from 1 to 5!")

for i in range(6):
    x = random.randint(0, 5)
    print(x)

print("Here are some numbers from 1 to 100!")

for i in range(6):
    x = random.randint(0, 100)
    print(x)

num1 = random.randint(0, 10)
num2 = random.randint(0, 10)

if (num1 == num2):
    print("The random numbers were the same!")
if (num1 != num2):
    print("The random numbers were different! Not too surprising, acatually.")
