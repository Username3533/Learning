#Ch10 - Files and Exceptions

""" with open('pi_million_digits.txt') as file_object:
    contents = file_object.readlines()

print(contents.strip())

pi_string = ''

for line in contents:
    pi_string += line.strip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

birthday =  input('Enter your birthday in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday is included in the first million digits of Pi!')
else:
    print('Your birthday is not included in the first millino didgits of Pi. :(') """

""" with open('learning_python.txt') as learningpython:
    contents = learningpython.readlines()

python = ""
for line in contents:
    python += line
    
print(python.replace('python', 'Javascript')) """

""" filename = 'programming.txt'

with open(filename, 'r+') as file:
    file.write('\nI love learning python!')
    file.write('\nIt has been such a great experience so far!') """

#append a file to collect data from user input
""" filename = 'guests.txt'

with open(filename, 'a') as file:
    name = input('What is your name? ')
    file.write(name)
    file.write('\n')

print(f'Welcome {name}!') """

#write all the reasons someone finds programming fun, storing the data in a text file on new lines.
""" filename = 'whyprogramming.txt'

with open(filename, 'a') as file:


    active = True
    while active: 
        message = input('Why do you like programming? ') 
        
        if message == 'quit':
            print('Thank you for your input!')
            active = False
 
        else:
            file.write(message)
            file.write('\n') """

""" print('Enter two numbers and they will be added together. Type "q" to quit.')

active = True
while active == True:
    num1 = input('Please enter your first number: ')
    num2 = input('Please enter your second number: ')

    if num1 == 'q':
        break
    elif num2 == 'q':
        break
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print('Please only enter numbers.')
    else:
        print(f'{num1} plus {num2} is equal to: {sum}') """



