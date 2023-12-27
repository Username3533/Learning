#Work With Dictionaries

""" alien_0 = {
    'color' : 'green',
    'points' : 5,
}

alien_0['x polsition'] = 25
alien_0['y position'] = 0

print(alien_0)

person = {
    'first name' : 'jack',
    'last name' : 'doe',
    'age' : 32,
    'sex' : 'male',
    'location' : 'california',
}

print(person) """

fav_numbers = {
    'scott' : 22,
    'kony' : 7,
    'richard' : 117,
    'billy' : 21
}

#first try looping
""" for person in fav_numbers:
    key = fav_numbers.get(person)
    print(f'{person.title()} : {key}') """

#more consise loop through dictionary
""" for key, value in fav_numbers.items():
    print(f'{key.title()} : {value}') """

friends = ['richard']

#comparing data in a dictionary with a list
for name in fav_numbers:
    print(f'Hi {name.title()}!')

    if name in friends:
        number = fav_numbers[name]
        print(f'Hi {name.title()}, your favorite number is {number}!')

if 'jack' not in fav_numbers:
    print('Jack, what is your favorite number?')

#sorted loop
for name in sorted(fav_numbers.keys()):
    print(f'Thank you {name.title()} for sharing your favorite number!')