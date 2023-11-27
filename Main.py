#importing the classes from Animal
from Animal import Cat, Dog, Zoo, ZooKeeper
#called zookeeper who is assigning to the zoo
zoo = Zoo()
zoo_keeper = ZooKeeper(assigned_zoo = zoo)
cat = Cat(name="Whiskers", age=3)
dog = Dog(name="Buddy", age=2)
# and add both animals and telling them to speak
zoo_keeper.add_animal(cat)
zoo_keeper.add_animal(dog)

zoo.make_all_animals_speak()
