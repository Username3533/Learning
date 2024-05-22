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




