# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): # it will inherit all the attributes and methods from its parent class which is "Animal"
    pass

class Cat(Animal): # it will inherit all the attributes and methods from its parent class which is "Animal"
    pass

class Mouse(Animal): # it will inherit all the attributes and methods from its parent class which is "Animal"
    pass

def run():
    dog = Dog("Scooby")
    cat = Cat("Garfield")
    mouse = Mouse("Jerry")

    print(dog.name)
    print(dog.is_alive)
    dog.eat()
    print()
    
    print(cat.name)
    print(cat.is_alive)
    cat.eat()
    print()
    
    print(mouse.name)
    print(mouse.is_alive)
    mouse.eat()
    print()