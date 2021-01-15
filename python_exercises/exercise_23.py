# One Shot Hi-Lo

import random
number = random.randint(0, 100)
print("I'm thinking of a number between 1-100. Try to guess it.")

guess = int(input("> "))

if (guess < number):
    print("Sorry, you are too low. I was thinking of", number)
elif (guess > number):
    print("Sorry, you are too high. I was thinking of", number)
elif (guess == number):
    print("You guessed it! What are the odds?!?")
else:
    print("HI-LO Error")
