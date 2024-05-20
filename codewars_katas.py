""" RGB to hex colors """

# def rgb(r, g, b):
#     # your code here :)
    
#     r = max(0, min(r, 255))
#     g = max(0, min(g, 255))
#     b = max(0, min(b, 255))    
    
    
#     r1 = int(r/16)
#     r2 = r%16
#     g1 = int(g/16)
#     g2 = g%16
#     b1 = int(b/16)
#     b2 = b%16

#     hex_value = [r1, r2, g1, g2, b1, b2]

    
    

#     conv = {
#         10: 'A',
#         11: 'B',
#         12: 'C',
#         13: 'D',
#         14: 'E',
#         15: 'F'
#     }

#     def convert(value):
#         if value < 10:
#             return str(value)
#         else:
#             return conv[value]
        
#     hex_value = convert(r1) + convert(r2) + convert(g1) + convert(g2) + convert(b1) + convert(b2)

#     return hex_value

# print(rgb(-20, 0, 0))

""" Pig latin converter """

# def pig_it(text):
#     #your code here
#     sentence = text.split()

#     def alpha_check(word):
#         if word.isalpha():
#             return word[1:] + word[0] + 'ay'
#         else:
#             return word
        
#     pigified = [alpha_check(i) for i in sentence]

#     new_sent = " ".join(pigified)

#     return new_sent
    

# text='screw you guys im going home !'
# print(pig_it(text))

# message = 'aBcdefghIjklmnopQustuvwxyz'

# # print([ord(char) for char in string.lower()])

# def decode_rot13(m2):
#     decoded_chars = []
#     for char in m2:
#         decoded = ord(char) + 13
#         if char.islower():
#             if decoded > ord('z'):
#                 decoded -= 26
#         elif char.isupper():
#             if decoded > ord('Z'):
#                 decoded -= 26
#         else:
#             decoded = ord(char)
#         decoded_chars.append(chr(decoded))
#     return ''.join(decoded_chars)

""" Pin brute force """

#1357 is the combo
#1 can be also 2 or 4
#3 can also be 2 or 6
#5 can also be 2 4 6 or 8
#7 can also be 4 or 8
#135 possible combos

# A = ['1', '2', '4']
# B = ['3', '2', '6']
# C = ['5', '2', '4', '6', '8']
# D = ['7', '4', '8']

# def generate_combinations(lst, current='', depth=0):
#     if depth == 4:
#         if 1 <= len(current) <= 8:
#             print(current)
#         return
#     for item in lst[depth]:
#         generate_combinations(lst, current + item, depth + 1)
#         if len(current + item) <= 8:
#             generate_combinations(lst, current + item, depth)

# generate_combinations([A, B, C, D])

""" 
1. Find all the prime factors present in the given array.
2. For each prime factor, calculate the sum of all the array elements for which it is a prime factor.
3. Construct the result array with each entry containing a prime factor and its corresponding sum. 
"""

num = [12, 15]
factors = []
for item in num:
    for number in range(2, item):
        if item % number == 0:
            factors.append(number)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0  or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

for factor in factors[:]:
    if not is_prime(factor):
        factors.remove(factor)

print(factors)

def sum_by_prime_factors(arr):
    prime_sum = {}
    for number in arr:
        for prime in is_prime(number):
            if prime in prime_sum:
                prime_sum[prime] += number
            else:
                prime_sum[prime] = number
    return prime_sum

sum_by_prime_factors()