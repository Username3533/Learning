""" Concepts include:
Async programming
Pandas
Browser automation, DOM manipulation
Argparse module
SQLite3
Convolutional neural networks
Image recognition
Coroutines
Arrays
table insertion/querying
Pandas
NumPy
Data encryption/manipulation/visualization
Deep learning
HTML/HTTP parsing/nav/routing
Json parsing
DataFrames
Log levels
Logging
ML/Natural language processing
Object mapping SQL
CSV files
APIs/HTTP requests
Server-client architecture
SMTP servers/email auth
Socket programming
Asymmetric/symmetric encryption
POS tagging/Tokenization/Stemming
Flask framework, dev, integration and APIs
Webscraping
 """

import array
import asyncio
import argparse
import requests
import re
import sqlite3
import csv
import json
import logging
import pandas as pd
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
import requests
import os
import socket
import smtplib
import nltk
from nltk import pos_tag
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from PIL import Image
from flask import Flask, jsonify, request, render_template
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from cryptography.fernet import Fernet
from selenium import webdriver
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import SGD
from keras.datasets import mnist
from keras.utils import to_categorical
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout



# """ Async coroutine event loop """
# async def say_hello():
#     print('Hello')
#     await asyncio.sleep(1)
#     print('World')

# async def main():
#     await asyncio.gather(say_hello(), say_hello())

# asyncio.run(main())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Pandas stuff """
# mean = df['olumn_name'].mean()
# std = df['column_name'].std()
# df['column_name'].plot(kind='line')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ web driver using selenium - needs work, first attempt"""
# driver = webdriver.Chrome()
# driver.get('https://www.the66project.net')

# element = driver.find_element("css selector", '#search')
# element.send_keys('python')

# form = driver.find_element("css selector",'#search-form')
# form.submit()

# driver.implicitly_wait(10)

# links = driver.find_elements("css selector", '.result a')
# links[0].click()

# driver.implicitly_wait(10)

# print(driver.title)

# driver.quit()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ CLI creation using Argparse """
# parser = argparse.ArgumentParser(description='Description of your script')
# parser.add_argument('-f', '--file', type=str, required=True, help='Path to the inpyt file')
# parser.add_argument('-n', '--number', type=int, default=10, help='Number ofitems to process')
# args = parser.parse_args()

# print(args.file)
# print(args.number)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Connecting to database using SQLite3 """
# conn = sqlite3.connect('example.db')

# c = conn.cursor()
# c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
# c.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', ('John', 'john@example.com'))
# c.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', ('Jane', 'jane@example.com'))

# conn.commit()
# conn.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# (X_train, y_train), (X_test, y_test) = mnist.load_data()

# X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
# X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))
# X_train = X_train.astype('float32') / 255
# X_test = X_test.astype('float32') / 255
# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)

# model = Sequential()
# model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
# model.add(MaxPooling2D((2, 2)))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D((2, 2)))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(Flatten())
# model.add(Dense(64, activation='relu'))
# model.add(Dense(10, activation='softmax'))

# model.compile(optimizer=SGD(learning_rate=0.01), loss='categorical_crossentropy', metrics=['accuracy'])

# model.fit(X_train, y_train, epochs=5, batch_size=64)

# loss, accuracy = model.evaluate(X_test, y_test)

# print('Loss: ', loss)
# print('Accuracy: ', accuracy)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# """ Coroutines """

# async def say_hello():
#     print('Hello')
#     await asyncio.sleep(1)
#     print('World')

# asyncio.run(say_hello())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Arrays """
# a = array.array('i', [1, 2, 3, 4, 5])

# print(a)
# print(a.typecode)
# print(len(a))

# a[2] = 6
# b = a[1:4]
# c = array.array('i', [6, 7, 8])
# d = a + c

# print(a)
# print(b)
# print(d)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Tables and Data """

# conn = sqlite3.connect('table.db')
# c = conn.cursor()

# c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# c.execute("INSERT INTO users VALUES (1, 'John', 30)")
# c.execute("INSERT INTO users VALUES (2, 'Jane', 25)")

# conn.commit()
# conn.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# import matplotlib.pyplot as plt

# Connect to the SQLite database
# conn = sqlite3.connect('table.db')
# cursor = conn.cursor()

# # Execute SQL query to retrieve data
# cursor.execute("SELECT name, age FROM users")
# rows = cursor.fetchall()

# Extract data into lists
# names = [row[0] for row in rows]
# ages = [row[1] for row in rows]

# conn.close()

# Create bar plot using Matplotlib
# plt.figure(figsize=(8, 6))
# plt.bar(names, ages, color='skyblue')
# plt.xlabel('Name')
# plt.ylabel('Age')
# plt.title('Age Distribution of Users')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ 3D array """
# a = np.array([[[1, 2, 3, 4, 5], 
#               [5, 4, 3, 2, 1], 
#               [1, 2, 3, 2, 1]],
              
#               [[13, 21, 31, 41, 5],
#               [21, 12, 3, 5, 4],
#               [55, 66, 77, 88, 99]]])

# print(a)
# print(a.shape)
# print(a.dtype)

# b = a + 1
# c = a * 2
# d = np.sqrt(a)
# e = np.sum(a)

# print(b)
# print(c)
# print(d)
# print(e)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Data encryption """

# key = Fernet.generate_key()

# cipher = Fernet(key)

# data = b'some plain text data'
# encrypted_data = cipher.encrypt(data)

# print(encrypted_data)

# decrypted_data = cipher.decrypt(encrypted_data)

# print(decrypted_data)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Data manipulation - numpy/pandas """

# arr = np.array([[1, 2], 
#                 [3, 4], 
#                 [5, 6]])

# print(arr)
# print(arr.shape)

# print(np.mean(arr))
# print(np.std(arr))

# df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35], 'gender': ['F', 'M', 'M']})

# print(df)
# df_filtered = df[df['age'] >= 30]

# print(df_filtered)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Data prep/Model training/Prediction - scikit """

# iris = load_iris()

# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)

# new_data = [[5.1, 3.5, 1.4, 0.2], [6.2, 2.9, 4.3, 1.3], [7.7, 3.8, 6.7, 2.2]]
# new_predictions = clf.predict(new_data)

# print('New data:', new_data)
# print('New predictions:', new_predictions)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Deep Learning using Keras """


# iris = load_iris()

# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)

# model = Sequential()
# model.add(Dense(units=10, activation='relu', input_dim=4))
# model.add(Dense(units=3, activation='softmax'))

# sgd = SGD(learning_rate=0.01)
# model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])

# model.fit(X_train, y_train, epochs=100, batch_size=32)

# loss, accuracy = model.evaluate(X_test, y_test)

# print('Loss:', loss)
# print('Accuracy:', accuracy)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Send email using SMTP and TLS encryption """

# subject = 'Test email'
# body = 'this is a test email'
# sender_email = 'test@hotmail.com'
# receiver_email = 'test@gmail.com'
# message = f'Subject: {subject}\n\n{body}'

# smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

# smtp_server.starttls()

# smtp_server.login(sender_email, 'password')

# smtp_server.sendmail(sender_email, receiver_email, message)

# smtp_server.quit()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Event loop """

# async def say_hello():
#     print('Hello')
#     await asyncio.sleep(1)
#     print('World')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(say_hello())
# loop.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Widnow using Tkinter """

# window = tk.Tk()

# label = tk.Label(window, text='Hello, Tkinter!')

# label.pack()

# window.mainloop()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ PyQt window """

# app = QApplication([])

# widget = QWidget()
# layout = QVBoxLayout()
# label = QLabel('Hello, World!')
# layout.addWidget(label)
# widget.setLayout(layout)
# widget.show()

# app.exec_()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ HTML Parsing using soup """

# html = """
# <html>
#     <head>
#         <title>My Page</title>
#     </head>
#     <body>
#         <h1>Welcome to my page!</h1>
#         <p>This is some text.</p>
#         <ul>
#             <li>Item 1</li>
#             <li>Item 3</li>
#             <li>Item 2</li>
#         </ul>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html, 'html.parser')

# title = soup.title

# h1 = soup.h1

# li = soup.li

# lis = soup.find_all('li')

# print(title.text)
# print(h1.text)
# print(li.text)
# for li in lis:
#     print(li.text)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Soup """
# html = '<html><body><h1>Hello, World!</h1></body></html>'
# soup = BeautifulSoup(html, 'html.parser')

# with open('example.html') as f:
#     soup = BeautifulSoup(f, 'html.parser')

# h1_element = soup.find('h1')
# text = h1_element.text
# print(text)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return 'This is a GET request'
#     elif request.method == 'POST':
#         return 'This is a POST request'
    
# if __name__ == '__main__':
#     app.run()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# response = requests.get('https://www.google.com')
# html_cotntent = response.text

# print(html_cotntent)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Pillow Lib """

# """ Crop """
# image = Image.open('image.jpg')
# image = image.crop((100, 100, 300, 300))
# image.save('image_cropped.jpg')

# """ Rotate """
# image = Image.open('image.jpg')
# image = image.rotate(45)
# image.save('image_rotated.jpg')

# """ Change format """
# image = Image.open('image.jpg')
# image.save('image.png')

# """ Resize """
# image = Image.resize((500, 500))

# """ Grayscale """
# image = Image.convert('L')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Parsing using json.loads() """
# json_string = '{"name": "John", "age": "30", "city": "New York"}'
# data = json.loads(json_string)

# print(data['name'])
# print(data['age'])
# print(data['city'])


# """ Generate JSON string from Python dictionary using json.dumps() """
# data = {"name": "John",
#         "age": "30",
#         "city": "New York"}

# json_string = json.dumps(data)
# print(json_string)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Line plots """

# x = [1, 2, 3, 4, 5]
# y = [10, 8, 6, 4, 2]

# fig, ax = plt.subplots()

# ax.plot(x, y, label='My line plot')

# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_title('My plot')
# ax.legend()

# plt.show()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Pandas DF loaded from CSV """

# # Load data
# df = pd.read('data.csv')

# print(df.head())

# # filter data in column A
# filtered = df[df['A'] > 10]

# # calc mean of column B and C
# grouped = df.groupby('B')['C'].mean()

# # sort A in descending order
# sorted = df.sort_values('A', ascending=False)

# #save modified data to csv

# filtered.to_csv('filtered.csv')
# grouped.to_csv('grouped.csv')
# sorted.to_csv('soretd.csv')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Logging """

# logging.basicConfig(filename='example.log', level=logging.DEBUG)

# logging.debug('Debug message')
# logging.info('Info message')
# logging.warning('Warning message')
# logging.error('Error message')
# logging.critical('Critical message')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Scikit-Learn supervised learning using Iris data set for prediction using Decision Trees """

# #load iris function
# iris = load_iris()

# #split data set into training and test set

# X_train, X_test, y_train, y_test =  train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# #set and train decision tree classifier
# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)

# #predict test set based on training set results
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)

# print('Accuracy:', accuracy)

# """ Accuracy results 1.0, probliem wit overfitting...probably """

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Natural Language proccessing using NLTK """

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('vader_lexicon')

# text = 'Learning python is awesome!.'

# #tokenize
# tokens = word_tokenize(text)

# #remove stopwords
# stop_words = set(stopwords.words('english'))
# filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# #Lemmatize filtered tokens
# lemmatizer = WordNetLemmatizer()
# lemmatized_toekns = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# #sentiment analysis
# analyzer = SentimentIntensityAnalyzer()
# scores = analyzer.polarity_scores(text)

# #results
# print('Original text:', text)
# print('Tokenized text:', tokens)
# print('Filtered text:', filtered_tokens)
# print('Lemmatized text:', lemmatized_toekns)
# print('Sentiment scores:', scores)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ OOP using classes """

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print(f'Hello, my name is {self.name} and I am {self.age} years old.')

# p = Person('John', 30)
# p.say_hello()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Object relational mapping using SQLAlchemy """

# # Create database engine and session
# engine = create_engine('sqlite:///example.db')
# Session = sessionmaker(bind=engine)
# session = Session()

# # Define database table
# Base = declarative_base()
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String)

# # Create database table
# Base.metadata.create_all(engine)

# # Add info to database
# user1 = User(name='John', email='john@example.com')
# user2 = User(name='Jane', email='jane@example.com')
# session.add(user1)
# session.add(user2)
# session.commit()

# users = session.query(User).all()
# for user in users:
#     print(user.name, user.email)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Pattern matching/substitution """

# string = 'My email is john@example.com and my friend\'s email is jane@example.com.'
# redacted = re.sub(r'\b[\w.-]+@[\w.-]+\.[\w.-]+\b', 'redacted', string)
# print(redacted)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Data querying SQL """

# conn = sqlite3.connect('example.db')

# c = conn.cursor()

# c.execute("SELECT * FROM users")
# rows = c.fetchall()
# for row in rows:
#     print(row)

# conn.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ CSV data filtering creating a list of dictionaries """

# with open('data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     data = [row for row in reader if row['score'] > '90']

# for row in data:
#     print(row['name'], row['score'])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Write to a text file """


# with open('new_file.txt', 'w') as f:
#     f.write('This is a new file!')

# with open('new_file.txt', 'a') as file:
#     file.write('Hello, again!')

# with open('new_file.txt', 'w') as f:
#     f.write('HeEEEELLLLLLLLLLOOOOOOOOOOO!!!!!')

# with open('new_file.txt', 'r') as f:
#     content = f.read()

# os.remove('new_file.txt')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Read Data from CSV using Pandas """

# df = pd.read_csv('data.csv')

# first_few_rows = df.head()

# column_mean = df['column_name'].mean()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ re - matching/replaceing """

# string = 'The Cat in the Hat'
# match = re.search('cat', string.lower())
# if match:
#     print('Match found:', match.group(0))

# new_string = re.sub('cat', 'dog', string.lower())
# print('New String:', new_string.title())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ RESTful API/Flask framework """

# response = requests.get('https://api.example.com/resource')
# data = response.json()

# app = Flask(__name__)

# users = [
#     {'id': 1, 'name': 'john', 'email': 'john.example.com'}
#     {'id': 2, 'name': 'jane', 'email': 'jane.example.com'}
#     {'id': 3, 'name': 'bob', 'email': 'bob.example.com'}
# ]

# @app.route('/users', method=['GET'])
# def get_users():
#     return jsonify(users)

# @app.route('/users/<int:user_id>', method=['GET'])
# def get_user(user_id):
#     for user in users:
#         if user['id'] == user_id:
#             return jsonify(user)
#     return jsonify({'error': 'User not found'})

# @app.route('/users', methods=['POST'])
# def create_user():
#     user = request.json
#     user['id'] = len(users) + 1
#     users.append(user)
#     return jsonify(user)

# @app.route('/users/<int:user_id>', methods=['PUT'])
# def update_user():
#     user = request.json
#     for i, u in enumerate(users):
#         if u['id'] == user_id:
#             users[i] = user
#             return jsonify(user)
#     return jsonify({'error': 'User not found'})

# @app.route('/users/<int:user_id', methods=['DELETE'])
# def delete_user(user_id):
#     for i, user in enumerate(users):
#         if user['id']:
#             del users[i]
#             return jsonify('message': 'User deleted')
#     return jsonify({'error': 'User not found'})

# if __name__ == '__main__':
#     app.run()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ String patterns """

# pattern = r'\d+'

# text = 'There are 123 apples and 456 oranges.'
# matches = re.findall(pattern, text)

# print(matches)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Server Client architecture """

# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()
# port = 9999

# serversocket.bind((host, port))

# serversocket.listen(1)

# clientsocket, address = serversocket.accept()

# clientsocket.send('Hello Client!'.encode())

# clientsocket.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Connect to server """

# host = socket.gethostname()
# port = 9999

# serversocket.connect((host, port))

# data = clientsocket.recv(1024)

# print(data.decode())

# clientsocket.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostbyname()

# port = 12345

# s.bind((host, port))

# s.listen(5)

# client_socket, client_address = s.accept()
# print('Got connection from', client_address)

# message = 'Thank you for connecting'
# client_socket.send(message.encode())

# client_socket.close()

# s.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Tokenization, stemming, POS tags """

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# text = 'The quick brown foxes jumped over the lazy dogs.'

# tokens = word_tokenize(text)

# stemmer = SnowballStemmer('english')
# stemmed_tokens = [stemmer.stem(word) for word in tokens]

# pos_tags = pos_tag(tokens)

# print('Original text:', text)
# print('Tokenized text:', tokens)
# print('Stemmed text:', stemmed_tokens)
# print('POS tags:', pos_tags)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ API with Flask """

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World!'

# @app.route('/api/data')
# def data():
#     data = {'name': 'john', 'age': 30, 'city': 'San Diego'}
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Flask Web Dev """

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return render_template('about.html')

# if __name__ == '__main__':
#     app.run()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Beautiful Soup web scraping """

# response = requests.get('https://www.example.com')

# soup = BeautifulSoup(response.content, 'html.parser')

# links = soup.find_all('a')

# for link in links:
#     print(link.get('href'))



# def get_robots_txt(url):
#     robots_url = f"{url}/robots.txt"
#     response = requests.get(robots_url)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return f"Failed to fetch robots.txt: {response.status_code}"

# website_url = 'https://www.bodybuilding.com'
# robots_txt = get_robots_txt(website_url)
# print(robots_txt)


# response = requests.get('https://www.example.com')

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     links = soup.find_all('a')
#     for link in links:
#         print(link.get('href'))
# else:
#     print(f"Failed to fetch webpage: {response.status_code}")


# url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
# response = requests.get(url)
# html = response.content

# soup = BeautifulSoup(html, 'html.parser')

# table = soup.find('table', {'class': 'wikitable sortable'})
# rows = table.findAll('tr')
# for row in rows:
#     cols = row.findAll('td')
#     for col in cols:
#         print(col.text.strip())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# """ Web scraping with Selenium """

# driver = webdriver.Chrome()
# driver.get('https://www.example.com')

# driver.implicitly_wait(10)

# element = driver.find_element_by_css_selector('#header')
# print(element.text)

# button = driver.find_element_by_css_selector('#load-more')
# button.click()

# driver.implicitly_wait(10)

# elements = driver.find_element_by_css_selector('.item')
# for element in elements:
#     print(element.text)

# driver.quit()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# def on_button_click():
#     label.config(text='Button clicked!')

# window = tk.Tk()

# label = tk.Label(window, text='Hello, Tkinter!')

# label.pack()

# button = tk.Button(window, text='Click me!', command=on_button_click)

# button.pack()

# window.mainloop()