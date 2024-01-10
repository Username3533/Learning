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


def make_album(artist, album_name, numoftracks = None):
    album = {'artist' : artist, 'album name' : album_name, 'number of tracks' : numoftracks}
    return album

print(make_album('Linkin Park', 'Meteora', 13))


