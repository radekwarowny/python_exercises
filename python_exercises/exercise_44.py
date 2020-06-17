import random

num = random.randint(0, 5)
cookie = ""

if (num == 1):
    cookie = "A beautiful, smart, and loving person will be coming into your life."
elif (num == 2):
    cookie = "A dubious friend may be an enemy in camouflage."
elif (num == 3):
    cookie = "A faithful friend is a strong defense."
elif (num == 4):
    cookie = "A feather in the hand is better than a bird in the air."
elif (num == 5):
    cookie = "A fresh start will put you on your way."

print("Fortune cookie says: " + cookie)

for i in range(6):
    x = random.randint(0, 54)
    print(x, end=" - ")
