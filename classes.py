#working with classes #review

""" class Dog:
    Making a dog

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting.')

    def rollover(self):
        print(f'{self.name} rolls over.')

my_dog = Dog('Sadie', 8)
my_dog.sit()
my_dog.rollover()

gooddog = Dog('Dixie', 12)

gooddog.sit()
gooddog.rollover()
print(f'{gooddog.name}, whos a good puppy?') """

""" class Restaurant:

    def __init__(self, name, cousine):
        self.name = name
        self.cousine = cousine
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.name} is a new restaurant that serves {self.cousine}!')
    
    def open_restaurant(self):
        print(f'{self.name} is now open and proudly serving {self.cousine} food!')

    def read_guests(self):
        print(f'{self.number_served} guests have been served.')

    def set_number_served(self, happy_guests):
        if happy_guests >= self.number_served:
            self.number_served = happy_guests
        else:
            print('You cant go back in time and served less people.')     

    def increment_number_served(self, new_customers):
        self.number_served += new_customers
        

class Ice_Cream_Stand(Restaurant):

    def __init__(self):
        self.flavors = ['Cherry', 'Chocolate', 'Strawberrry', 'Chocolate Chip', 'Mint']

    def get_flavors(self):
        for flavor in self.flavors:
            print(f'The available flavors include {flavor}.')

basic_ice_stand = Ice_Cream_Stand()

basic_ice_stand.get_flavors()
basic_ice_stand.set_number_served(20)
basic_ice_stand.read_guests() """

""" Asian_infusion = Restaurant('Asiafu', 'Asian Infusion')
Asian_infusion.describe_restaurant()
Asian_infusion.open_restaurant()

continental = Restaurant('Continental', 'Continental')
continental.describe_restaurant()
continental.open_restaurant()

continental.set_number_served(20)
continental.read_guests()
continental.increment_number_served(15)
continental.read_guests() """



""" class User:
    
    def __init__(self, user_name, age, sex, hobby):
        self.user_name = user_name
        self.age = age
        self.sex = sex
        self.hobby = hobby

    def desc_user(self):
        print(f'{self.user_name} is a {self.age} year old {self.sex} who enjoys {self.hobby}.')

aeacus = User('Aeacus', 32, 'male', 'gaming')
korgen = User('Korgen', 33, 'male', 'kickin ass')
aeacus.desc_user()
korgen.desc_user() """

