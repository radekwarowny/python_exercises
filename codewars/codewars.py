''' codewars challenges '''

""" challenge 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
"""


def challenge1(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])


number = 10
#print("Challenge 1 answer is: ", challenge1(number))



""" challenge 2
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(s):
    result = [i for i in s if i.isalpha()]
    if len(result) >= 26:
        return True
    return False

pangram = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"

#print("Challenge 2 answer is: ", is_pangram(pangram))

""" challenge 3
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...] But what if we started with [0, 0, 1] as a signature? 
As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, 
you may be tempted to think that we would get the same sequence shifted by 2 places, 
but that is not the case and we would get: [0, 0, 1, 1, 2, 4, 7, 13, 24, ...] Well, you may have guessed it by now, but to be clear: 
you need to create a fibonacci function that given a signature array/list, 
returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, 
then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;) 
"""


def tribonacci(signature, n):
    
    if n > len(signature):
        signature.extend([sum(signature)])
        for i in range(n-4):
            signature.extend([sum(signature[i+1:])])
        return signature
    elif n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return signature[:2]
    return signature
         
#print("Challenge 3 answer is: ", tribonacci([1,1,1],1))

"""  challenge 4
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
"""


def challenge4(s):
    # i think it needs refactoring
    foo = []
    for i in range(len(s)):
        if len(s) % 2 != 0:
            s = s+'_'
        if i % 2 == 0:
            foo.append(s[i:i+2])
    return foo

test = "x"
#print(challenge4(test))


""" challenge 5
Requirements:
There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
"""

def zero(*args): 
    return '0', args
def one(*args): 
    return '1'
def two(*args): 
    return '2'
def three(*args):
    return '3'
def four(*args): 
    return 4
def five(*args): 
    if args:
        return '5', args
    return '5'
def six(*args): 
    return 6
def seven(*args):
    if args:
        return '7', args
    return '7'
def eight(*args):
    return 8
def nine(*args): 
    return 9

def plus(*args): 
    return '+', args
def minus(*args):
    return '-'
def times(*args):
    return '*' , str(args)
def divided_by(*args):
    return '//'

# not sure about the solution at this time

# def seven(*args):
#     print(*args)
#     if None:
#         return 7
#     return args
    
# def five(*args):
#     print(args)
#     if not args:
#         return 5
#     return args
    

# def times(*args):
#     return 
# print(seven(times(five())))

four(plus(nine()))
eight(minus(three()))
six(divided_by(two()))

""" challenge 5
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

"""

def domain_name(url):
    import re
    
    
    http = re.split('http://', url)
    https = re.split('https://', url)
    www = re.split('www.', url)

    
    def domain(x):
        foo = []
        for i in x[1]:
            if i != '.':
                foo.append(i)
            else:
                break
        return ''.join(foo)
    
    
    if len(http) > 1:
        return domain(http)
    elif len(https) > 1:
        return domain(https)
    elif len(www) > 1:
        return domain(www)
    else:
        return 'Invalid Input'
    




domain_name("http://google.com") # "google"
domain_name("http://google.co.jp") # "google"
domain_name("www.xakep.ru") # "xakep"
domain_name("https://youtube.com") # "youtube"    