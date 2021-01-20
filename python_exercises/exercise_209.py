""" exercise 209 Project Euler """
""" f the numbers 1 to 5 are written out in words:
    one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
    how many letters would be used? """


digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numbers = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = "hundred"
thousands = "one thousand"
_and = "and"
below_hundred = []
all_numbers = []
n = 1

while n < 11:
    if n == 1:
        for i in range(9):
            below_hundred.append(digits[i])
    elif n == 2:
        for i in range(10):
            below_hundred.append(teens[i])
    elif n > 2 or n < 10:
        below_hundred.append(numbers[n - 3])
        for i in range(9):
            tens = numbers[n-3] + ' ' + digits[i]
            below_hundred.append(tens)
    n += 1

over_hundred = []
foo = 0
while foo < 9:
    single_hundred = digits[foo] + ' ' + hundreds
    over_hundred.append(single_hundred)
    for i in range(0, 99):
        full_hundred = digits[foo] + ' ' + hundreds + ' ' + _and + ' ' + below_hundred[i]
        over_hundred.append(full_hundred)

    foo += 1
if foo == 9:
    over_hundred.append(thousands)

# for i in below_hundred:
#     print(i)
# print()
# for i in over_hundred:
#     print(i)
#
# print()
# print("Below hundred count: ", len(below_hundred))
# print("Over hundred count: ", len(over_hundred))
all_numbers = below_hundred + over_hundred
# print("All numbers count: ", len(all_numbers))


def count_letters(numbers):
    bucket = []
    for i in numbers:
        x = i.replace(' ', '')
        bucket.append(x)
    no_space = ''.join(bucket)
    print("Number of letters: ", len(no_space))


count_letters(all_numbers)










