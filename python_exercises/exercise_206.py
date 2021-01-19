""" exercise 206 Project Euler """
""" The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd) 
    
    Which starting number, under one million, produces the longest chain?"""



def collatz_sequence(n):

    terms = 0

    while n != 1:
        if n % 2 == 0:
            n = n//2
            terms += 1
        else:
            n = 3 * n + 1
            terms += 1

    return terms


terms_bucket = []


for i in range(10, 1000000-1):
    max_terms = (collatz_sequence(i), i)
    terms_bucket.append(max_terms)

max_term = max(terms_bucket)

print("Starting number: ", max_term[1])
print("Max term: ", max_term[0])

