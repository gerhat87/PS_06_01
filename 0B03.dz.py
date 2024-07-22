class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} ест")
    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Чирик")




class Mammal(Animal):
    def make_sound(self):
        print("гав")

class Reptile(Animal):
    def make_sound(self):
        print("пшш")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self, animals, workers):  
            self.animals = []
            self.workers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"животное {animal} добавлено")

    def add_workers(self, new_worker):
        self.workers.append(new_worker)
        print(f"работник {new_worker} добавлен")

class ZooKeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник кормит {animal.name}")

class Veterinarian():
    def heal_animal(self, animal):
        print(f"Ветеренар лечит {animal.name}")

zoo = Zoo("animal","workers")

bird1 = Bird("тица", 1)
mammal1 = Mammal("собака", 2)
reptile1 = Reptile("гига",3)

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)


zooKeeper1=ZooKeeper()
veterinarian1 = Veterinarian()

zoo.add_workers(zooKeeper1)
zoo.add_workers(veterinarian1)

animal_sound(zoo.animals)

zooKeeper1.feed_animal(bird1)
veterinarian1.heal_animal(mammal1)