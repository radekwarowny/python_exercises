''' codewars challanges '''

""" Challange 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
"""

def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])
    

number = 10
# print(solution(number))


""" Challange 2
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

# print(is_pangram(pangram))


""" Challange 3
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
    return [signature[0]]
         
print(tribonacci([0,0,1],3))
