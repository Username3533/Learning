#Fun with If #review

""" banned_users = ['jack', 'jill', 'mark']

user = "jack"
if user in banned_users:
    print(f"Sorry {user.title()}, you have been banned.")

user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you are not banned.")

car = "audi"
print(car == 'chevy') #does equal test
print(car != 'chevy') #does not equal test

'chevy' > 'audi'
print("chevy" > "audi")

age = 16
if age >= 18:
    print("You are allowed to vote.")
else:
    print("Sorry, you must wait until you are 18 years old.")

if age < 4:
    price = 10
elif age < 18:
    price = 20
else:
    price = 40

print(f"Because you are {age} years old, your ticket costs ${price}.") """

""" usernames = ['admin', 'user1', 'maverick', 'bosscat', 'monkeyman'] """

""" for user in usernames:
    if user == 'admin':
        print(f'Hello {user}, would you like a status update?')
    if user != 'admin':
        print(f'Welcome back {user}, how are you doing today?') """

""" usernames = []

if usernames:
    for user in usernames:
        print(f"Hello, {user}!")
else:
    print("Admin! We need users!") """

""" new_users = ['User1', 'jack', 'Maverick', 'roger', 'doger']

for user in new_users:
    if user.lower() in copy_users:
        print(f"Sorry, {user.title()} is already taken. Please choose another username.")
    else:
        print(f"Welcome {user.title()}!") """

""" numbers = [value * 1 for value in range(1, 10)]
print(numbers)

for value in numbers:
    if value == 1:
        print(f"{value}st")
    elif value == 2:
        print(f"{value}nd")
    elif value == 3:
        print(f"{value}rd")
    else:
        print(f"{value}th") """

#alien game

""" alien1 = ['green']
alien2 = ['yellow']
alien3 = ['red']

if 'green' in alien1:
    print("The alien you just killed is worth 5 points!")
elif 'yellow' in alien1:
    print("The alien you just killed is worth 10 points!")
elif 'red' in alien1:
    print("The alien you just killed is worth 15 points!")

if 'green' in alien2:
    print("The alien you just killed is worth 5 points!")
elif 'yellow' in alien2:
    print("The alien you just killed is worth 10 points!")
elif 'red' in alien2:
    print("The alien you just killed is worth 15 points!")

if 'green' in alien3:
    print("The alien you just killed is worth 5 points!")
elif 'yellow' in alien3:
    print("The alien you just killed is worth 10 points!")
elif 'red' in alien3:
    print("The alien you just killed is worth 15 points!") """

""" age = 32

if age < 2:
    print(f"This person is {age} years old, they are a baby.")
elif age <= 4:
    print(f"This person is {age} years old, they are a toddler.")
elif age <= 13:
    print(f"This person is {age} years old, they are a kid.")
elif age <= 20:
    print(f"This person is {age} years old, they are a teenager.")
elif age < 65:
    print(f"This person is {age} years old, they are an adult. (Theoretically)")
elif age >= 65:
    print(f"This person is {age} years old, they are aan elder.") """

""" favorite_fruits = ['mango', 'apple', 'cherry']

if 'bannana' in favorite_fruits:
    print("Wow, you really like bannanas!")
    
if 'cherry' in favorite_fruits:
    print("Wow, you really like cherries!")

if 'mango' in favorite_fruits:
    print("Wow, you really like mangos!")

if 'apple' in favorite_fruits:
    print("Wow, you really like apples!")

if 'guava' in favorite_fruits:
    print("Wow, you really like guavas!") """
