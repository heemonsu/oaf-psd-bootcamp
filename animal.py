## Write abstract class Animal with two implementations Cat & Dog
## Share private attributes: name, age
## Abstract method: speak() -> prints individual message
#Parent Class for Animal Objects

# animal.py

# Parent Class for Animal Objects
class Animal:

    def __init__ (self,name,age):
        self.name = name
        self.age = age

    # Abstract method
    def speak(self):
        pass

# Implement two concrete subclasses of Animal: Cat and Dog
class Cat(Animal):
    def speak(self):
        print(f"{self.name} the cat says 'Meow'")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} the dog says 'Woof'")

# Implement the Zoo class
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def speak_all(self):
        for animal in self.animals:
            animal.speak()
# l love python programming
# Implement the ZooKeeper class
class ZooKeeper:
    def __init__(self, zoo):
        self.zoo = zoo

    def add_animal(self, animal):
        self.zoo.add_animal(animal)
