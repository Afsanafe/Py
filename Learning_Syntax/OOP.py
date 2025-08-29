# Object Orientated Programming in Python

class Car:
    # the 'self' parameter or first paramater can technically be named anything - it refers to the instance
    def __init__(self, model, year, color, for_sale): # Constructor method (dunder method, dunder = double underscore)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self): # Method to drive

    

def run():
    car1 = Car("Mustang", 2024, "red", False)

    car2 = Car("Corvette", 2025, "blue", True)
    print(car1.model)
    print(car1.year)
    print(car1.color)
    print(car1.for_sale)

    print(car2.model)
    print(car2.year)
    print(car2.color)
    print(car2.for_sale)
