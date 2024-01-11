#Fun with functions

""" def Hello():
  print('Hello World!')

Hello()

def greet_user(username):
  print(f"Hello, {username.title()}!")

greet_user('marshal')

def message():
  print('I am learning about functions!')

message()

def favorite_book(title):
  print(f'One of my favorite books is {title.title()}!')

favorite_book('gone with the wind') """

""" def make_shirt(size = 'large', text = 'I love Python'):
    print(f'Your {size} shirt will read "{text}"!')

make_shirt('large', 'Big Whoop, wanna fight about it?')
make_shirt(size = 'extra medium', text = 'Cool Story Bro')
make_shirt() """


""" def make_album(artist, album_name, numoftracks = None):
    album = {'artist' : artist, 'album name' : album_name, 'number of tracks' : numoftracks}
    return album

print(make_album('Linkin Park', 'Meteora', 13)) """



#uses one list for an action and puts item in a new list
""" def print_messages(messages, sent_messages):
    while messages:
        sent_message = messages.pop()
        sent_messages.append(sent_message)
        
        

messages = ['You are learning Python', 'How long do you think it will be until you are ready for a job?', 'This is a test']
sent_messages = []
print_messages(messages[:], sent_messages)
print(sent_messages)
print(messages) """


#creates a tuple with unlimited args
""" def create_sandwich(*toppings):
    print('\nThis sandwich will have:')
    print(f'- {toppings}')

create_sandwich('turkey', 'lettuice', 'tomatoes', 'mustard')
create_sandwich('ham', 'cheese')
create_sandwich('bacon', 'lettuice', 'tomatoes') """


#creates dictionary with unlimited args
""" def build_profile(first, last, **profile):
    profile['firstname'] = first
    profile['lastname'] = last
    return profile

profile = build_profile('scott', 'holder', age=35, sex='male')
print(profile) """


#just ordered a new truck :)
""" def make_car(model, make, **car):
    car['model'] = model
    car['make'] = make
    return car

new_car = make_car('dodge', 'ram', fully_loaded='Laramie package', color='ruby red')
print(new_car) """