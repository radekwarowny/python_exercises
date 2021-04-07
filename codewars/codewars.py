#!/usr/bin/env python

"""codewars.py: Results of Codewars katas."""

__author__      = "Radek Warowny"
__email__   = "radekwarownydev@gmail.com"

''' codewars challenges '''

# Classes
""" challenge 1
Define a method/function that removes from a given array of integers all the values contained in a second array.
"""

class List:
    def remove_(self, integer_list, values_list):
        result = []
        for i in integer_list:
            if i in values_list:
                pass
            else:
                result.append(i)
        return result
    
l = List()
integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
values_list  = [1, 3, 4, 2]
l.remove_(integer_list, values_list)

""" challenge 2
We need a method in the List Class that may count specific digits from a given list of integers. 
This marked digits will be given in a second list. 
The method .count_spec_digits()/.countSpecDigits() will accept two arguments, 
a list of an uncertain amount of integers integers_lists/integersLists (and of an uncertain amount of digits, too) and a second list, 
digits_list/digitsList that has the specific digits to count which length cannot be be longer than 10 (It's obvious, 
we've got ten digits). 
The method will output a list of tuples, each tuple having two elements, the first one will be a digit to count, 
and second one, its corresponding total frequency in all the integers of the first list. 
This list of tuples should be ordered with the same order that the digits have in digitsList
"""

class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        result = []
        str_ints = [] # ints broken down to string of digits
        n = 0
        while n < len(integers_list):
            str_int = str(integers_list[n])
            for i in str_int:
                str_ints.append(i)
            n += 1
        
        for i in digits_list:
            dig_count = str_ints.count(str(i))
            result.append((i,dig_count))
        return result
    
l = List()

integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]
l.count_spec_digits(integers_list, digits_list)


""" challenge 3
The following code was thought to be working properly, 
however when the code tries to access the age of the person instance it fails.

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)

For this exercise you need to fix the code so that it works correctly.
"""

class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = f"{first_name} {last_name}"

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)


""" challenge 4
In this kata, your job is to create a class Dictionary which you can add words to and their entries. 
Example:

>>> d = Dictionary()
>>> d.newentry('Apple', 'A fruit that grows on trees')
>>> print(d.look('Apple'))
A fruit that grows on trees
>>> print(d.look('Banana'))
Can't find entry for Banana
"""

class Dictionary():
    def __init__(self):
        self.dictionary = dict()
    def newentry(self, word, definition):
        self.dictionary[word] = definition
    def look(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        return f"Can't find entry for {key}"
    
d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')

print(d.look('Apple'))
print(d.look('Banana'))

""" challenge 5
A company is opening a bank, but the coder who is designing the user class made some errors. They need you to help them.

You must include the following:

    A withdraw method
        Subtracts money from balance
        One parameter, money to withdraw
        Raise a ValueError if there isn't enough money to withdraw
        Return a string with name and balance(see examples)

    A check method
        Adds money to balance
        Two parameters, other user and money
        Other user will always be valid
        Raise a ValueError if other user doesn't have enough money
        Raise a ValueError if checking_account isn't true for other user
        Return a string with name and balance plus other name and other balance(see examples)

    An add_cash method
        Adds money to balance
        One parameter, money to add
        Return a string with name and balance(see examples)

Additional Notes:

    Checking_account should be stored as a boolean
    No input numbers will be negative
    Output must end with a period
    Float numbers will not be used so, balance should be integer
    No currency will be used

Examples:

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

Jeff.withdraw(2) # Returns 'Jeff has 68.'

Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

Jeff.check(Joe, 80) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

Joe.check(Jeff, 100) # Raises a ValueError

Jeff.add_cash(20.00) # Returns 'Jeff has 118.'
"""

class User:
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def withdraw(self, value):
        if self.balance < value: raise ValueError()
        self.balance -= value
        return "{} has {}.".format(self.name, self.balance)
    
    def add_cash(self, value):
        self.balance += value
        return "{} has {}.".format(self.name, int(self.balance))
    
    def check(self, other, value):
        if other.checking_account:
            s1, s2 = other.withdraw(value), self.add_cash(value)
            return "{} and {}".format(s2, s1)
        raise ValueError()
    

    
Jeff = User('Jeff', 70, True)   
Joe = User('Joe', 70, False)

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

Jeff.withdraw(2) # Returns 'Jeff has 68.'

Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

Jeff.check(Joe, 80) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

Joe.check(Jeff, 100) # Raises a ValueError

Jeff.add_cash(20.00) # Returns 'Jeff has 118.'

""" challenge 6
A keyword cipher is a monoalphabetic cipher which uses a "keyword" to provide encryption. 
It is somewhat similar to a Caesar cipher.
In a keyword cipher, repeats of letters in the keyword are removed and the alphabet is reordered such that the letters in the keyword appear first, 
followed by the rest of the letters in the alphabet in their otherwise usual order.

E.g. for an uppercase latin alphabet with keyword of "KEYWORD":

A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z

becomes:

K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z

such that:

cipher.encode('ABCHIJ') == 'KEYABC'
cipher.decode('KEYABC') == 'ABCHIJ'

All letters in the keyword will also be in the alphabet. 
For the purpose of this kata, only the first occurence of a letter in a keyword should be used. 
Any characters not provided in the alphabet should be left in situ when encoding or decoding.
"""

class keyword_cipher(object):
    def __init__(self, abc, keyword):
        self.abc = abc
        self.keyword = keyword
        self.code = []
        
        for i in keyword:
            self.code.append(i)
        
        for i in abc: 
            if i not in keyword: self.code.append(i)
                
    def encode(self, plain):
        result = []
        for i in plain:
            index = self.abc.index(i)
            print(self.code[index], end='')
            result.append(self.code[index])
        return ''.join(result)
    
    def decode(self, ciphered):
        result = []
        for i in ciphered:
            index = self.code.index(i)
            print(self.abc[index], end='')
            result.append(self.abc[index])
        return ''.join(result)

abc = "abcdefghijklmnopqrstuvwxyz"
key = "keyword"
cipher = keyword_cipher(abc, key)

cipher.encode("abc") # "key");
cipher.encode("xyz") # "vxz");
cipher.decode("key") # "abc");
cipher.decode("vxz") # "xyz");


""" challenge 7

Professor Oak has just begun learning Python and he wants to program his new Pokedex prototype with it.
For a starting point, he wants to instantiate each scanned Pokemon as an object that is stored at Pokedex's memory. 
He needs your help!

Your task is to:
Create a PokeScan class that takes in 3 arguments: name, level and pkmntype.
Create a info method for this class that returns some comments about the Pokemon, 
specifying it's name, an observation about the pkmntype and other about the level.
Keep in mind that he has in his possession just three Pokemons for you to test the scanning function: Squirtle, 
Charmander and Bulbasaur, of pkmntypes water, fire and grass, respectively.
The info method shall return a string like this: Charmander, a fiery and strong Pokemon.
If the Pokemon level is less than or equal to 20, it's a weak Pokemon. 
If greater than 20 and less than or equal to 50, it's a fair one. If greater than 50, it's a strong Pokemon.
For the pkmntypes, the observations are wet, fiery and grassy Pokemon, according to each Pokemon type.
"""

class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):
        # Power level
        if self.level <= 20:
            level = "weak"
        elif self.level > 20 <= 50:
            level = "fair"
        elif self.level > 50:
            level = "strong"
        else:
            level = "difficult to define."

        # Level
        if self.pkmntype == "water":
            pkmntype = "wet"
        elif self.pkmntype == "fire":
            pkmntype = "fiery"
        elif self.pkmntype == "grass":
            pkmntype = "grassy"

        print(f"{self.name}, a {pkmntype} and {level} Pokemon.")
        return f"{self.name}, a {pkmntype} and {level} Pokemon."



PokeScan('Squirtle', 0, 'water').info()
PokeScan('Squirtle', 21, 'water').info() # 'Squirtle, a wet and fair Pokemon.')
PokeScan('Squirtle', 50, 'water').info() # 'Squirtle, a wet and fair Pokemon.')
PokeScan('Squirtle', 51, 'water').info() # 'Squirtle, a wet and strong Pokemon.')
PokeScan('Squirtle', 100, 'water').info() # 'Squirtle, a wet and strong Pokemon.')



# Algorithms

""" challenge 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
"""

def challenge1(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])

number = 10
# print(challenge1(number))


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

# print(is_pangram(pangram))

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
         
#print(tribonacci([1,1,1],1))

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

""" challenge 6
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. 
Square all numbers k (0 <= k <= n) between 0 and n. 
Count the numbers of digits d used in the writing of all the k**2. Call nb_dig (or nbDig or ...) 
the function taking n and d as parameters and returning this count.
"""

def nb_dig(n, d):
    foo = []
    count = 0
    for i in range(0, n+1):
        k = i * i
        if str(d) in str(k): 
            foo.append(k)
            for i in str(k):
                if i == str(d):
                    count += 1
                
    print("Count", count)
    return count

nb_dig(5750, 0)
nb_dig(11011, 2)
nb_dig(12224, 8)
nb_dig(11549, 1)

""" challenge 7
Tap code is a way to communicate using a series of taps and pauses for each letter. 
In this kata, we will use dots . for the taps and whitespaces for the pauses.
The number of taps needed for each letter matches its coordinates in the following polybius square (note the c/k position).
Then you "tap" the row, a pause, then the column. 
Each letter is separated from others with a pause too.

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z

"""

def tap_code_translation(text):
    import string
    
    polybius = """1  2  3  4  5
    1  A  B C\K D  E
    2  F  G  H  I  J
    3  L  M  N  O  P
    4  Q  R  S  T  U
    5  V  W  X  Y  Z"""
    
    result = ' '
    
    alpha = string.ascii_lowercase # alphabet
    letters = []
    f_letters = []

    for i in polybius:
        if i.lower() in alpha:
            letters.append(i)
    letters_str = ' '.join(letters) 
    
    # removing 'c' and 'k' for 'c/k'
    letters_str = letters_str.replace('C', '')
    letters_str = letters_str.replace('K', 'C/K')
    letters_str = letters_str.replace('  ', ' ')

  
    foo = letters_str.split(' ')

    n = 1
    m = 1
    for i in foo:
        bar = f"{m} {n} {i}"
        f_letters.append(bar)
     
        n += 1
        if n > 5:
            n=1
            m += 1
    
    result = []
    for i in text:
        for j in f_letters:
                for t in j:
                    if i.upper() in t:
                        one = int(j[0])
                        two = int(j[2])
                        one_dash = f"{'.'*one} "
                        two_dash = f"{'.'*two} "
                        result.append(one_dash)
                        result.append(two_dash)
                        print('.'*one, '.'*two, end=' ')
 
    result = ''.join(result)
    print(result[:-1])
    return result[:-1]
