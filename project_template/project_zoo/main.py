# # import abstract base class module
# # import abstractmethod module


from abc import ABC, abstractmethod


# create an abstract base class Animal
class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @abstractmethod  # decorator
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print(f"{self._name}, the cat, says: Meow!")


class Dog(Animal):
    def speak(self):
        print(f"{self._name}, the dog, says: Woof!")


class Zoo:
    def __init__(self):
        self.animals = []

    def speak_all(self):
        for animal in self.animals:
            animal.speak()


class Zookeeper:
    def __init__(self, zoo):
        self.zoo = zoo

    def add_animal(self, animal):
        self.zoo.animals.append(animal)
        print(
            f"Added {animal._name}, a {animal.__class__.__name__.lower()}, to the zoo."
        )


print("Creating a zoo!")
my_zoo = Zoo()

print("Creating a zookeeper!")
zookeeper = Zookeeper(my_zoo)

print("Creating animals!")
cat = Cat("Whiskers", 3)
dog = Dog("Rover", 5)

print("Adding animals to the zoo via the zookeeper!")
zookeeper.add_animal(cat)
zookeeper.add_animal(dog)

print("The animals speak!")
my_zoo.speak_all()
