""" Basic python exercises """
import math

#Calculate area of a circle using input after checking if input is valid
# def circle_area():
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

#Convert Cecius to Fahrenheit or vice versa
# def convert_temp():
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

