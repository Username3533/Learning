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
import sqlite3
import pandas
from selenium import webdriver
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import SGD
from keras.datasets import mnist
from keras.utils import to_categorical



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