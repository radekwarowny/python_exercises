# A Dumb Calculator

num_1 = float(input("What is your first number: "))
num_2 = float(input("What is your second number: "))
num_3 = float(input("What is your third number: "))
total = (num_3 + num_2 + num_3) / 2
print()
print("({:.2f} + {:.2f} + {:.2f}) / 2 is... {:.2f} ".format(num_1, num_2, num_3, total))
