# Still Using Variables

myName = "Juan Valdez"
gradDate = "2010"

print("My name is {} and I'll graduate in {}.".format(myName, gradDate))

# refactored

myName, gradDate = "Radek Warowny", 2020
print(f"\nMy name is {myName} and I have graduated in {gradDate}.")
