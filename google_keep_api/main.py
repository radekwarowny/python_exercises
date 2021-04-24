# Reqirement: 
# pip3 install gkeepapi


import csv
import gkeepapi

keep = gkeepapi.Keep()
success = keep.login('example@gmail.com', 'password')

gnotes = keep.all()

exercises = []

n = 1
for i in gnotes:

    single_ex = i.text.split('\n')
    exercises.append(single_ex)
    n += 1

for i in range(len(exercises)):
    while ('' in exercises[i]):
        exercises[i].remove('')

result = sum(exercises, [])
for i in result:
    print(i)
