# How Old Are You, Specifically?

name = input("Hey, what's your name? (Sorry, I keep forgettin.) ")
age = int(input("Ok, {}, how old are you? ".format(name)))
print()

if (age < 16):
    print("You can't drive.")
elif(age >= 16 and age <= 17):
    print("You can drive but not vote.")
elif(age >= 18 and age <= 24):
    print("You can vote but not rent a car.")
elif(age > 25):
    print("You can do pretty much anything. ")
else:
    print("Input Error")
