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

""" fav_numbers = {
    'scott' : 22,
    'kony' : 7,
    'richard' : 117,
    'billy' : 21
} """

#first try looping
""" for person in fav_numbers:
    key = fav_numbers.get(person)
    print(f'{person.title()} : {key}') """

#more consise loop through dictionary
""" for key, value in fav_numbers.items():
    print(f'{key.title()} : {value}') """

""" friends = ['richard']

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
    print(f'Thank you {name.title()} for sharing your favorite number!') """

#nesting
""" alien0 = {'color' : 'green', 'points' : 5}
alien1 = {'color' : 'yellow', 'points' : 10}
alien2 = {'color' : 'red', 'points' : 15}

#aliens = [alien0, alien1, alien2]

aliens = []

for alien_number in range(30):
    alien = alien0
    aliens.append(alien)

#change charactaristics of dictionary in list and add new key/value
for alien in aliens[:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium' """

#remove first 5 items and add 5 new items
""" for alien in aliens[:5]:
    if alien == alien0:
        aliens.remove(alien)
        aliens.insert(0, alien1) """

#print(aliens[:5])

people = []


person1 = {
    'first name' : 'jack',
    'last name' : 'doe',
    'age' : 32,
    'sex' : 'male',
    'location' : 'california',
    'favorite_locations' : ['palm springs', 'san diego']
}
person2 = {
    'first name' : 'jane',
    'last name' : 'doe',
    'age' : 34,
    'sex' : 'female',
    'location' : 'florida',
    'favorite_locations' : ['vegas', 'river']
}
person3 = {
    'first name' : 'maximus',
    'last name' : 'meridius',
    'age' : 44,
    'sex' : 'male',
    'location' : 'rome',
    'favorite_locations' : ['rome', 'pompeii', 'florence']
}

people.append(person1)
people.append(person2)
people.append(person3)

for person in people:
    print(f'{person['first name']} {person['last name']} is a {person['age']} year old {person['sex']} who lives in {person['location']}.')

for person in people:
    if person['sex'] == 'male':
        print(f'He likes to spend time in {person['favorite_locations']}.')
    elif person['sex'] == 'female':
        print(f'She likes to spend time in {person['favorite_locations']}.')