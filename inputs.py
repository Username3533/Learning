#working with user inputs #review2

#parrot
""" parrot = input('Tell me something and I will repeat it: ')
print(parrot) """

""" preffered_car = input('What kind of car would you like to rent? ')
print(f'Okay, let me see if I can find you a {preffered_car}') """

""" table = input('How many are in your group? ')
table = int(table)

if table >= 8:
    print("I'm sorry, we do not have a table of that size redily available, please wait while we get one ready.")
else:
    print("We have a table for that group size ready, please take a seat.") """

""" multiple = input("Pick a number, any number: ")
multiple = int(multiple)

if multiple % 10 == 0:
    print('That number is divisable by 10!')
else:
    print("That number sucks, pick a multiple of 10!") """

#parrot loop
""" prompt = "\nTell me something and I will repat it back to you!" #variable with string to be printed by loop
prompt += "\nType 'quit' to stop. " #+= used on a variable

message = "" #placeholder variable for input

while message != 'quit': #if user types anything beside 'quit', keep running loop
    message = input(prompt) #redefines variable with empty string inside loop and displays the prompt string variable as message for input
        
    if message != 'quit:    
        print(message) """

#parrot loop with flag for ending loop
""" prompt = "\nTell me something and I will repat it back to you!"
prompt += "\nType 'quit' to stop. "

message = "" 

active = True
while active: 
    message = input(prompt) 
        
    if message == 'quit':  
        active = False

    else:
        print(message) """

#Add a pizza topping loop to a list
""" prompt = "\nTell me what you want on your pizza!"
prompt += "\nType 'quit' to stop. "

message = "" 
pizzatoppings = []

active = True
while active: 
    message = input(prompt) 
        
    if message == 'quit':
        print(pizzatoppings)
        active = False

    else:
        pizzatoppings.append(message)
        print(message) """

#user data stored in dictionary using inputs
""" user = {}

active = True

while active:
    name = input('What is your name? ')
    user['name'] = name

    age = input('How old are you? ')
    user['age'] = int(age)

    sex = input('Are you male or female? ')
    user['sex'] = sex

    if input() == 'quit':
        print(user)
        active = False """
