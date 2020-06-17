# A Little Quiz

choice = input("Are you ready for a quiz? ")
yes = ['Yes', 'yes', 'Y', 'y']
if choice in yes:
    print("Okay, here it comes!")
else:
    print("No problemo. See you later.")
    quit()

score = 0

print("Q1) What is the capital of Alaska?")
print("1) Melbourne")
print("2) Anchorage")
print("3) Juneau")

answer = int(input("> "))
print()

if(answer == 1):
    print("That's incorrect.")

elif(answer == 2):
    print("That's correct.")
    score += 1
elif(answer == 3):
    print("Sorry, that's incorrect.")
else:
    print("Input Error.")
print()

print("Q2) Can you store the value \"cat\" in a variable of type int?")
print("\t1) yes")
print("\t2) no")

answer = int(input("> "))
print()

if(answer == 1):
    print("Sorry, \"cat\" is a string. Ints store numbers.")
elif(answer == 2):
    print("That's correct. ")
    score += 1
else:
    print("Incorrect Input.")
print()

print("Q1) What is the result of 9+6/3?")
print("\t1) 5")
print("\t2) 11")
print("\t3) 15/3")

answer = input("> ")

if(answer == 1):
    print("That's correct.")
    score += 1
elif(answer == 2):
    print("That's incorrect.")
elif(answer == 3):
    print("That's right.")
    score += 1
else:
    print("Incorrect Input.")

print()

print("Overall, you got {} out of 3 correct.".format(score))
print("Thatks for playing. ")
