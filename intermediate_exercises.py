""" This file is for practice exercises given an problem and finding a solution without looking at answers """

""" Exercise 1: scrape data from a website """

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.google.com'
# data = requests.get(url)

# parsed_data = BeautifulSoup(data.text, 'html.parser')

# links = parsed_data.find_all('a')
# for link in links:
#     print(link.get('href'))

# """ Exercise 2: Read and write data from a file (I/O) """

# with open('exercise2.txt', 'w') as f:
#     f.write('This is exercise 2...ez mode')

# with open('exercise2.txt', 'r') as file:
#     text = file.read()
#     upper = text.title()
#     print(upper)

# """ Exercise 3: using pandas to look at a CSV file """

# import pandas

# data = pandas.read_csv('example.csv')

# print(data.head())
# print(data.describe())
# print(data.median())
# print(data.sum())
# print(data.abs())
# print(data.min())
# print(data.max())
# print(data.aggregate())

# """ Exercise 4: Argparse script for CLI """

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('name', help='your name')
# parser.add_argument('age', type=int, help='your age')
# args = parser.parse_args()

# greeting = f'Hello, {args.name}! you are {args.age} years old.'
# print(greeting)

# """ Exercise 5: API """

# import requests

# url = 'https://api.example.com/data'
# request = requests.get(url)

# data = request.json()

# for info in data:
#     print(info)




# def avg(*args):
#     nums = []
#     for item in args:
#         nums.append(item)

#     avg = sum(nums) / len(nums)
#     print(f'{avg:.2f}')

# avg(2345, 123, 42134, 123, 4125, 6275)

# string = 'How are you doing today?'
# def check_chars(s):
#     asdf = [ord(char) for char in s]

#     for num in asdf[1:]:
#         current = asdf[i]
#         last = asdf[i-1]
#         if current > last:
#             chr(num).upper()
#             print(num)
#     print(asdf)
#     # def fun(st):
#     #     for char in st[1:]:
#     #         if char.isalpha():
#     #             ord(char)

    
    
    

# print(check_chars(string))


# def make_readable(seconds):
#     yy = seconds // ((24*3600) * 365)
#     dd = seconds // (24*3600) % 365
#     hh = seconds // 3600 % 24
#     mm = seconds % 3600 // 60
#     ss = seconds % 60
#     print(f'{yy:02}:{dd:02}:{hh:02}:{mm:02}:{ss:02}')

    
# make_readable(1716463019)


# def alnum(s):
#     return s.isalnum()

# def alpha_num(string):
#     nums = [ord(str(num)) for num in range(0, 10)]
#     letters = [ord(letter) for letter in 'abcdefghijklmnopqrstuvwxyz']
#     valid = set(nums + letters)
    

#     ord_str = [ord(str(char)) for char in string.lower()]

#     for char in ord_str:
#         if char not in valid:
#             return False        
#     return True
    
# string = 'what1235'

# print(alpha_num(string))


