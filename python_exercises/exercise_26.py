# Space Boxing

weight = int(input("Please enter your current earth weight (lbs): "))
print()
print("I have information for the following planets: ")
print("\t1. Venus    2. Mars    3. Jupiter")
print("\t4. Saturn   5. Uranus  6. Neptune")
print()

planet = int(input("Which planet are you visiting? "))
new_weight = 0

if (planet == 1):
    new_weight = weight * 0.78
elif(planet == 2):
    new_weight = weight * 0.39
elif(planet == 3):
    new_weight = weight * 2.65
elif(planet == 4):
    new_weight == weight * 1.17
elif(planet == 5):
    new_weight = weight * 1.05
elif(planet == 6):
    new_weight = weight * 1.23
else:
    print("Input Error.")

print()
print("Your weight would be {} pounds on tht planet.".format(new_weight))
