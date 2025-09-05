# object = A "bundle" of related attributes (variables) and methods (functions)
#           Ex. phone(whats the number, who's number is it, transmit calls, recieve calls), cup(whats in the liquid? how big is the cup?), book(what is the title of the book (title = "jobbit"))

# class = (blueprint) used to desing the structure and layout of an object

# Also for our logic where all our definitions are going inside of a run() function
# You can put the classes outside run() so the top-level classes can be imported from other modules and unit tests

from .car import Car

def run():

    car1 = Car("Mercedes", 2025, "Matte Black", False) # when you're creating an object you need to invoke the method with the same parameters, 
                                #  don't worry about passing self as an argument, thats done automatically, you just need to remmember to include self in the 'method signature' meaning method defintion

    print(car1.model)
    print(car1.year)
    print(car1.color)
    print(car1.for_sale)
    print()

    car2 = Car("Corvette", 2025, "red", True)

    print(car2.model)
    print(car2.year)
    print(car2.color)
    print(car2.for_sale)


    