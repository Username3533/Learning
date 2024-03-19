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

import asyncio
import argparse
import pandas
from selenium import webdriver


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

# """ Argparse """
# parser = argparse.ArgumentParser(description='Description of your script')
# parser.add_argument('-f', '--file', type=str, required=True, help='Path to the inpyt file')
# parser.add_argument('-n', '--number', type=int, default=10, help='Number ofitems to process')
# args = parser.parse_args()

# print(args.file)
# print(args.number)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

