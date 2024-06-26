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



# """ Exercise 6: Classes/Objects, encapsulation, inheritance """

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f'Hello, my name is {self.name} and I am {self.age} years old.')

# class Student(Person):
#     def __init__(self, name, age, major):
#         super().__init__(name, age)
#         self.major = major

#     def describe(self):
#         print(f'I am a student majoring in {self.major}.')

# person = Person('Alice', 25)
# person.greet()

# student = Student('Bob', 20, 'Computer Science')
# student.greet()
# student.describe()


# """ Exercise 7: Threading/Sync """

# import threading

# counter = 0
# lock = threading.Lock()

# def incrament():
#     global counter
#     with lock:
#         counter += 1

# threads = []
# for i in range(10):
#     t = threading.Thread(target=incrament)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print(f'The counter is {counter}.')

# """ Exercise 8: unit testing """

# import unittest

# def is_palendrome(s):
#     return s == s[::-1]

# class TestPalindrome(unittest.TestCase):
#     def test_is_palendrome(self):
#         self.assertTrue(is_palendrome('racecar'))
#         self.assertFalse(is_palendrome('hello'))

# if __name__ == '__main__':
#     unittest.main()


# """ Exercise 9: Data Viz """

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)

# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.title('Line chart')

# plt.show()

# """ Exercise 10: Data Ops """

# import sqlite3

# conn = sqlite3.connect('example.db')

# conn.execute('''CREATE TABLE IF NOT EXISTS users
#              (id INTEGER PRIMARY KEY,
#              name TEXT,
#              email TEXT)''')

# conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Alice', 'alice@example.com'))
# conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Bob', 'bob@example.com'))

# cursor = conn.execute('SELECT id, name, email FROM users')
# for row in cursor:
#     print(f'{row[0]} - {row[1]} ({row[2]})')

# conn.close()


# """ Exercise 11: Networking """

# #server side
# import socket

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 0000))
# server_socket.listen(1)

# while True:
#     client_socket, address = server_socket.accept()
#     data = client_socket.recv(1024)
#     response = data.upper()
#     client_socket.sendall(response)
#     client_socket.close()

# #client side
# import socket

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('localhost', 0000))
# client_socket.sendall(b'Hello, server!')
# response = client_socket.recv(1024)
# print(response)
# client_socket.close()

# """ Exercise 12: Data Science """

# import numpy as np
# import pandas as pd

# data = {'x': np.arange(10),
#         'y': np.random.randn(10)}

# df = pd.DataFrame(data)

# print('Df mean:', df.mean())
# print('DF standar dev', df.std())

# df['z'] = df['x'] * df['y']

# print(df)

# """ Exercise 13: Image Processing """

# from PIL import Image

# image = Image.open('image.jpg')

# print(image.format)
# print(image.size)
# print(image.mode)

# grayscale_image = image.convert('L')
# grayscale_image.show()

# resized_image = image.resize((300, 300))