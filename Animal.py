#used abc to import Abstract Base Class
from abc import ABC, abstractmethod
#Create an animal class with name and age attributes
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
#declaring the abstract method
    @abstractmethod
    def make_animalsound(self):
        pass
# created a cat animal class that makes a specific sound
class Cat(Animal):
    def make_animalsound(self):
        return f"{self.name} the Cat ({self.age} years old) says Meow!"

# created a dog animal class that makes a specific sound
class Dog(Animal):
    def make_animalsound(self):
       return  f"{self.name} the Dog ({self.age} years old) says Woof!"

# created a zoo class that takes in an arraylist of animals that is only mentioned in Animal class
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise ValueError("Only Animal objects can be added to the zoo.")
# created a method that allows all animals to speak at the same time
    def make_all_animals_speak(self):
        for animal in self.animals:
            print(animal.make_animalsound())
# created a Zookeeper class that adds an animal to the zoo
class ZooKeeper:
    def __init__(self, assigned_zoo):
        self.Zoo = assigned_zoo

    def add_animal(self, animal):
        self.Zoo.add_animal(animal)


