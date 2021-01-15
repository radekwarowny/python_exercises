# How Old Are You?

name = input("Hey, what's your name? ")
print()
age = int(input("Ok, {}, how old are you? ".format(name)))

if(age < 16):
    print("You can't drive.")
if(age < 18):
    print("You can't vote.")
if(age < 25):
    print("You can't rent a car.")
if(age > 25):
    print("You can do anything that's legal.")
