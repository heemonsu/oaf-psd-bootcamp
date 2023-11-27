class Animal():

    def __init__(self, name: str, age: int)  -> None:
        self.name = name
        self.age = age

    def who(self) -> None:
        print('name : ', self.name,  '\nage : ', self.age)

class Cat(Animal):
    def speak(self) -> None:
        print("I am a cat. Meow.")

class Dog(Animal):
    def speak(self) -> None:
        print("I am a dog. Woof.")

class Zoo():
    def __init__(self, list: list=[]) -> None:
        self.list = list

    def speakAll(self) -> None: 
        for element in self.list:
            element.speak()
            element.who()


class ZooKeeper():
    def __init__(self, Zoo: Zoo) -> None:
        self.Zoo = Zoo

    def add_animal(self, Animal) -> None:
        self.Zoo.list.append(Animal)

spiffy = Cat("spiffy", 32)
spiffy.who()
#spiffy.speak()
pem = Dog("Pem", 40)
pem.who()
#pem.speak()
list1 = [spiffy, pem] 
zoo = Zoo(list1)
zoo = Zoo(list=[spiffy, pem])


zanimal = Cat("zanimal", 100)

zooMan = ZooKeeper(zoo)
zooMan.addAnimal(zanimal)

zoo.speakAll()
