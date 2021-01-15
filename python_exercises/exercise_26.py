import random

num = random.randint(0, 10)

print("I'm thinking of a number from 1 to 10.")
guess = int(input("Your guess: "))

if (num == guess):
    print("That's right! My secret number was " + str(num))
else:
    print("Sorry, but I was really thinking of " + str(num))
