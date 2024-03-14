""" Basic python exercises """
import math


# def circle_area():
#     """ Calculate area of a circle using input after checking if input is valid """
#     radius = input('What is the radius of the circle? ')
#     try:
#         radius = float(radius)
#         area = math.pi * (radius ** 2)
#         print(f'The area of the circle is {area}.')
#     except ValueError:
#         print('Please try again and enter a valid number, or you will be stuck in this circle (get it?) forever! MUAHAHAHAHAHAHA!')
#         circle_area()

# circle_area()


#Count the number of times a word appears in a string
# string = "What are you doing today? I hope you are going to the store today?"
# word_count = {}

# for word in string.lower().split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
        
# print('Word count: \n', word_count)


# def convert_temp():
#     """ Convert Cecius to Fahrenheit or vice versa """
#     try:
#         unit_of_measure = input('What is the current temperature measured in (C or F)? ')
#         temp = float(input('What is the temperature? '))
#         if unit_of_measure.upper() == 'C':
#             converted_f = temp * (9 / 5) + 32
#             print(f'{temp} in {unit_of_measure} is equal to {converted_f:.2f} in Fahrenheit.')
#         elif unit_of_measure.upper() == 'F':
#             converted_c = (temp - 32) * (5 / 9)
#             print(f'{temp} in {unit_of_measure} is equal to {converted_c:.2f} in Celcius.')
#         else unit_of_measure.upper() != 'C' or 'F':
#             print('Please enter valid fields.')
#     except:
#         print('Please enter valid fields.')

# convert_temp()



# def multiples():
#     """ Creates list of first ten multiples of input number """
#     number = int(input('Enter a number: '))
#     multiples = []
#     for i in range(1, 11):
#         multiples.append(number * i)
#     print(multiples)

# multiples()

# def calc_interest():
#     """ Calculates simple interets """
#     try:
#         principal = float(input('Enter principal amount: '))
#         rate = float(input('Enter interest rate: '))
#         years = float(input('Enter number of years: '))
        
#         interest = principal * rate * years / 100
#         total_amount = principal + interest
#         monthly = total_amount / (years * 12)

#         print(f'The simple interest is: {interest:.2f}')
#         print(f'The total amount is: {total_amount:.2f}')
#         print(f'The monthly payments are: {monthly:.2f}')

#     except ValueError:
#         print('Enter valid fields.')

# calc_interest()

# def fib_seq(n):
#     """ Calculate fibonacci sequence to n """
#     sequence = [0, 1]
    
#     for i in range(2, n):
#         sequence.append((sequence[-1]) + (sequence[-2]))
#     return sequence[:n]

# n = int(input('Enter the number of Fibs to generate: '))
# fib_nums = fib_seq(n)

# print(f'The first {n} nunbers of the fibonacci sequence are: {fib_nums}')

# year = int(input('Enter the year you wish to check if it is a leapyear: '))

# if year % 4 == 0:
#     print(f'{year} is a leap year.')
# else:
#     print(f'{year} is not a leap year, sorry.')

# number = int(input('What number would you like to check the prime status of? '))

# def chk_prime(number):
#     """ Check the prime status of a number """
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

# if chk_prime(number):
#     print(f'{number} is prime.')
# else:
#     print(f'{number} is not prime.')

# def char_chk():
#     """ Count number of occurances of a character in a string """
#     sample_str = input('Enter your string: ').lower()
#     vowels = 'aeiou'
#     similar = {}

#     for char in sample_str:
#         if char in vowels:
#             if char in similar:
#                 similar[char] += 1
#             else:
#                 similar[char] = 1

#     print(similar)

# char_chk()

# def factorial():
#     """ Find the factorial of a number """
#     factorial_result = 1
#     try:
#         number = int(input('Enter a number: '))
#         for i in range(1, number + 1):
#             factorial_result *= i
#         print(factorial_result)
#     except ValueError:
#         print('Enter a whole number.')

# factorial()


# def sum_of_digits():
#     """ Find sum of digits """
#     try:
#         number = input('Enter a number: ')
#         total = sum(int(digit) for digit in str(number))
#         print(total)
#     except ValueError:
#         print('Enter a whole number.')

# sum_of_digits()

#Modular sum of digits
# def sum_of_digits(number):
#     """ Modular version of finding the sum of digits """
#     try:
#         total = sum(int(digit) for digit in str(number))
#         print(total)
#     except ValueError:
#         print('Enter a whole number.')

# number = input('Please enter a number: ')
# sum_of_digits(number)

# def cesar_cipher(text, shift):
#     """ Basic Cesar Cipher, converts letters to unicode, shifts them, and returns encoded string """
#     encrypted_message = []

#     for char in text:
#         if char.isalpha():
#             shift_amount = shift % 26
#             new_ord = ord(char) + shift_amount

#             if char.islower():
#                 if new_ord > ord('z'):
#                     new_ord -= 26
#             else:
#                 if new_ord > ord('Z'):
#                     new_ord -= 26

#             encrypted_message.append(chr(new_ord))
#         else:
#             encrypted_message.append(char)

#     return "".join(encrypted_message)

# text = input('What message would you like to encrypt? ')
# shift = int(input('Cipher shift amount: '))

# encoded_text = cesar_cipher(text, shift)
# print(f'{encoded_text}')



# def find_longest_word(words):
#     """ Find the longest word in a string """
#     longest_word = ""
#     max_length = 0

#     for word in words:
#         if len(word) > max_length:
#             max_length = len(word)
#             longest_word = word
    
#     print(f'The longest word is: {longest_word}')

# input_sentence = input('Enter a sentence: ')
# words = input_sentence.split()

# find_longest_word(words)


# """ Avg numbers in a lsit """
# numbers = [float(x) for x in input('Enter a list of numbers: ').split()]

# avg = sum(numbers) / len(numbers)
# print(f'The average of the numbers given is: {avg:.2f}')

# """ Converts lists to sets and compares them """
# list1 = input('Enter a list of numbers: ').split()
# list2 = input('Enter a second list of numbers: ').split()

# common = set(list1) & set(list2)
# print(f'Common numbers are: {common}')

# list_of_nums = input('Enter a list of numbers: ').split()

# max = max(list_of_nums)
# min = min(list_of_nums)

# print(f'Max is {max}')
# print(f'Min is {min}')

# """ Remove duplicates from list and print unique items """
# input_list = input('Enter a list of elements: ').split()
# unique = list(dict.fromkeys(input_list))
# print(f'{unique}')


# """ Create, square and cube a list using comprehension """
# range_size = int(input('Enter a whole number: '))
# numbers = [1 * num for num in range(1, range_size + 1)]

# print(numbers)
# squared_nums = [num **2 for num in numbers]
# cubed_nums = [num ** 3 for num in numbers]
    
# print(squared_nums)
# print(cubed_nums)