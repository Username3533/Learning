#Fun with If

banned_users = ['jack', 'jill', 'mark']

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

print(f"Because you are {age} years old, your ticket costs ${price}.")