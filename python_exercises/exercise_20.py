# BMI Calculator

height = float(input("Your height in m: "))
weight = int(input("Your weight in kg: "))
print()
bmi = weight / (height * height)
print()
print("Your BMI is {:.1f}.".format(bmi))
