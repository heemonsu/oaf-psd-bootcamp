"""
Professional SW Dev - OpenAvenues

Write abstract class Animal with two implementations Cat & Dog
    Share private attributes: name, age
    Abstract method: speak() -> prints individual message
Implement class Zoo
    Attribute: list of Animal objects
    Method: speak_all() (calls speak method for each animal in the current instance)
Implement class ZooKeeper
    Attribute: single Zoo instance
    Method: add_animal(animal: Animal) (adds an animal to the assigned zoo)
At each step, add print statements to showcase behavior
Run your code by creating instances of all classes, calling all methods at least once
"""

from abc import ABC, abstractmethod
def main():
     # define base class
    class Animal(ABC):
        """An abstract base/parent class for Animal objects"""
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @abstractmethod
        def speak(self):
            pass

    #define sub class
    class Cat(Animal):
        """A cat instance of Animal"""
        def speak(self):
            print (f"{self.name} the cat age {self.age} says meow!")
        
    class Dog(Animal):
        """A dog instance of Animal"""    
        def speak(self):
            print (f"{self.name} the dog age {self.age} says woof!")

    # Show implementation - cat and dog instances of Animal class
    cat = Cat("Taby", 4)
    dog = Dog("Max", 5)

    # overriding speak() method of Animal class
    cat.speak()
    dog.speak()

    # Show implementation - more instances of Animal class
    class Zebra(Animal):
        """A zebra instance of Animal"""
        def speak(self):
            print ("\t" + f"{self.name} says bray!")

    class Elephant(Animal):
        """An elephant instance of Animal"""
        def speak(self):
            print ("\t" + f"{self.name} says trumpet!")

    class Giraffe(Animal):
        """A giraffe instance of Animal"""
        def speak(self):
            print ("\t" + f"{self.name} says bleat!")

    # Show implementation of doc string
    print("\n" + Zebra.__doc__ + "\n")

    # Create the Zoo class
    class Zoo:
        """A class named Zoo to create a list of Animal objects"""
        def __init__(self):
            self.animals = []

        def add_animal(self, animal):
            if isinstance(animal, Animal):
                self.animals.append(animal)
                print(f"{animal.name} age {animal.age} was added to the zoo.")
            else:
                print("Invalid object.")

        def speak_all(self): 
            for animal in self.animals:
                animal.speak()

    # Create animal instances for the zoo
    zebra = Zebra("Zany", 1)
    elephant = Elephant("Elly", 2)
    giraffe = Giraffe("Gigi", 3)

    # Create instance of Zoo class
    zoo = Zoo()

    class ZooKeeper:
        """A class named ZooKeeper to add Animal instances to the Zoo class list """
        def __init__(self, zoo):
            self.zoo = zoo
        
        def add_animal(self, animal):
            if isinstance(animal, Animal):
                self.zoo.add_animal(animal)
            else:
                print("Invalid object.")

    # Create instance of ZooKeeper and add
    zoo_keeper = ZooKeeper(zoo)
    zoo_keeper.add_animal(zebra)
    zoo_keeper.add_animal(elephant)
    zoo_keeper.add_animal(giraffe)

    # Show animals added to the Zoo class list
    print("\nZoo animals:")
    for animal in zoo.animals:
        print("\t"+ f"{animal.name} ({type(animal).__name__})")

    # Override Animals speak method for each animal in the zoo
    print("\nWhat do the zoo animals say?")
    zoo.speak_all()

if __name__ == '__main__':
    main()

   