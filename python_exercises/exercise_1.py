# More Variables and Printing

myName = "Zed A Shaw"
myAge = 35
myHeight = 74  # inches
myWeight = 180  # lbs
myEyes = "Blue"
myTeeth = "White"
myHair = "Brown"

print("Let's talk about {}".format(myName))
print("He's {} inches tall.".format(myHeight))
print("He's {} pounds heavy.".format(myWeight))
print("Actually, that's not too heavy.")
print("He's got {} eyes and {} hair.".format(myEyes, myHair))
print("His teeth are usually {} depending on the coffee".format(myTeeth))

# refactored

myName, myAge, myHeight, myWeight, myEyes, myTeeth, myHair = "Radek", 33, 74, 180, "Brown", "White", "Brown"

print("\nLet's talk about {}".format(myName))
print("He's {} inches tall.".format(myHeight))
print("He's {} pounds heavy.".format(myWeight))
print("Actually, that's not too heavy.")
print("He's got {} eyes and {} hair.".format(myEyes, myHair))
print("His teeth are usually {} depending on the coffee".format(myTeeth))
