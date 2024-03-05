""" Basic python exercises """
import math

#Calculate area of a circle using input and checking if input is valid
def circle_area():
    radius = input('What is the radius of the circle? ')
    try:
        radius = float(radius)
        area = math.pi * (radius ** 2)
        print(f'The area of the circle is {area}.')
    except ValueError:
        print('Please try again and enter a valid number, or you will be stuck in this circle (get it?) forever! MUAHAHAHAHAHAHA!')
        circle_area()

circle_area()