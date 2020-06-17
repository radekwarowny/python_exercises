# Three Card Monte

import random

print("You slide up to Fast Eddie's card table and plop down your cash.\r He glances at you out of the corner of his eye and starts shuffling.\r He lays down three cards.\n")

ace = random.randint(1, 3)

print("Which one is the ace?\n")
print("\t## ## ##")
print("\t## ## ##")
print("\t1  2  3\n")

choice = int(input("> "))
print()

if (choice != ace):
    print("Ha! Fast Eddie wins again! The ace was card number", ace)
else:
    print("You nailed it!. Fast Eddie reluctantly hands over your winnings, scorling.")

if (ace == 1):
    print("\tAA ## ##")
    print("\tAA ## ##")
    print("\t1  2  3")
elif (ace == 2):
    print("\t## AA ##")
    print("\t## AA ##")
    print("\t1  2  3")
elif (ace == 3):
    print("\t## ## AA")
    print("\t## ## AA")
    print("\t1  2  3")
