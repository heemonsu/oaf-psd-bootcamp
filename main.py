# main.py
# Import your classes
from animal import Animal, Cat, Dog, Zoo, ZooKeeper

# Create instances of your classes
cat1 = Cat("Whiskers", 3)
dog1 = Dog("Fido", 5)

zoo = Zoo()
zoo.add_animal(cat1)
zoo.add_animal(dog1)

zookeeper = ZooKeeper(zoo)

# Call methods on your instances
print("All animals in the zoo speak:")
zoo.speak_all()

print("\nAll animals in the zoo:")
zoo.speak_all()
