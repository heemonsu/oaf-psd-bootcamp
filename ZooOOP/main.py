#!/usr/local/bin/python3
"""
Steve Eckardt
oa professional software development bootcamp
revised: October 31st, 2023
Week 2 OOPs Zoo
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, age, speech):
        self.__name = name
        self.__age = age
        self.speech = speech

    def __str__(self):
        return f"{self._Animal__name}({self._Animal__age})"

    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):

    def speak(self):
        return f"{self} the cat says {self.speech}"

class Dog(Animal):

    def speak(self):
        return f"{self} the dog says {self.speech}"

class Zoo(ABC):

    def __init__(self):
        self.zoo = []

    def add_animal(self, animal: Animal):
        self.zoo.append(animal)

    def speak_all(self):
        result = []
        for animal in self.zoo:
            result.append(animal.speak())
        return result

class ZooKeeper(Zoo):

    def __init__(self):
        super().__init__()

    def __init__(self, zoo: Zoo):
        self.zoo = zoo.zoo

if __name__ == "__main__":

    print()
    cat = Cat('climber', 2, 'meow')
    print(cat.speak())
    dog = Dog('spot', 14, 'woof')
    print(dog.speak())

    zoo = Zoo()
    zoo.add_animal(cat)
    zoo.add_animal(dog)
    print('\nzoo all speak')
    for saying in zoo.speak_all():
        print(saying)

    keeper = ZooKeeper(zoo)
    keeper.add_animal(Cat('mittens', 7, 'mememe'))
    keeper.add_animal(Dog('hunter', 5, 'roof'))
    print('\nkeeper all speak')
    for saying in keeper.speak_all():
        print(saying)    
