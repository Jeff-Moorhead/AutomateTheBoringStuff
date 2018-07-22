#! python3

class Pet():
    def __init__(self, name, age, species):
        self.name = name
        self.species = species
        self.age = age

    def increment_age(self):
        self.age += 1
        return self.age

    def overrider(self):
        print('Hello -- not overridden')


class Dog(Pet):
    def __init__(self, name, age, size=''):
        super(Dog, self).__init__(name, age, species='Dog')
        self.size = size

    def bark(self):
        print('Woof woof')

    def overrider(self, name):
        super().overrider()
        print('Hello, this method is overridden.')
        print(f'My name is {name}')
