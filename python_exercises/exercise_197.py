''' exercise 197 Project Euler '''
''' What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? '''

def smallest_number():
    ''' Smallest number that can be divided by each of the numbers from 1 to 10 without reminder.'''
    
    num = 1
    n = 1
    score = 1

    while num < 3000:
        while n < 10:
            if num % n == 0:
                score += 1
                if score == 10:
                    result = num
            else:
                pass
            n += 1
        score = 1
        n = 1
        num += 1

    print("Result: ", result)





smallest_number()






