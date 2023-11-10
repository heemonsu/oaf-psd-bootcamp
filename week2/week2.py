class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who(self):
        print('name : ', self.name,  '\nage : ', self.age)

class Cat(Animal):
    def Speak(self):
        print("I am a cat. Meow.")
        
class Dog(Animal):
    def Speak(self):
        print("I am a dog. Woof.")

class Zoo():
    def __init__(self, list=[]):
        self.list = list

    def speak_all(self):
        for element in self.list:
            element.Speak()
            element.who()


class ZooKeeper():
    def __init__(self, Zoo):
        self.Zoo = Zoo
    
    def add_animal(self, Animal):
        self.Zoo.list.append(Animal)
            
spiffy = Cat("spiffy", 32)
spiffy.who()
#spiffy.Speak()
pem = Dog("Pem", 40)
pem.who()
#pem.Speak()
list1 = [spiffy, pem] 
zoo = Zoo(list1)
zoo = Zoo(list=[spiffy, pem])
# why can't we pass spiffy and pem to the zoo list like this... zoo = Zoo({spiffy, pem})
#zoo.speak_all()

zanimal = Cat("zanimal", 100)

zooMan = ZooKeeper(zoo)
zooMan.add_animal(zanimal)

zoo.speak_all()
