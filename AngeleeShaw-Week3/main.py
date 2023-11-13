from abc import ABC, abstractmethod

# Abstract class Animal with two implementations : Cat & Dog
# Abstract Methods : speak() that prints a message
class Animal(ABC): 
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self._name} says meow"

class Dog(Animal):
    def speak(self):
        return f"{self._name} says woof"
    
# Implement class Zoo with all 
# Attributes : list of Animal objects...
# Methods : speak_all() that calls speak method for each animal in current instance
class Zoo(): 
    def __init__(self):
        self.animals = []

    def speak_all(self):
        for animal in self.animals:
            print(animal.speak())

# Implement class ZooKeeper
# Attributes : single Zoo instance
# Methods : add_animal that adds an animal to the assigned zoo
class ZooKeeper():
    def __init__(self, zoo):
        self.zoo = zoo

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.zoo.animals.append(animal)
        else:
            print('This animal does not meet the criteria needed to be added to a Zoo')

    def check_inventory(self):
        print(self.zoo.animals)

# Create instances of Animal subclasses
cat = Cat("Frank", 10)
dog = Dog("Spot", 3)

# Create a Zoo and a ZooKeeper
zoo = Zoo()
zookeeper = ZooKeeper(zoo)

# Add animals to the Zoo using the ZooKeeper
zookeeper.add_animal(cat)
zookeeper.add_animal(dog)
zookeeper.check_inventory()

# Make all the animals in the Zoo speak
zoo.speak_all()
