class Car:
    def __init__(self, model, year, color, for_sale): # this is our constructure method , dunder and initialize, we need this method to create objects, and similar to functions
                                                        # also the 'self' instance, is a convention for the first parameter of an instance method,
                                                        # you could name it anything but *always use self*
                                                        # if you don't include you WILL get a type error
                                                        # So: use self to read/write instance state and call other instance methods; it’s Python’s explicit way of saying “this method operates on this object.”
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drove the {self.color} {self.model}") # self in the placeholder is referring to the object we are currently working with, and access one of our attributes

    def stop(self):
        print(f"You stopped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

'''
- __init__ runs on instantiation and creates instance attributes by assigning to self.x = ....
- Those attributes live on the instance (e.g., obj.__dict__), not on the class.
- Calling obj.method() is sugar for Class.method(obj)—Python auto-passes the instance as the first arg.
- You declare self in the method signature so the method can access that instance; you don’t pass it explicitly.
- Any instance method can read/write the attributes created in __init__ via self.attr.
- Class variables are defined at class level and are shared across instances (unless shadowed by an instance attribute).
- Forgetting self in a method signature → TypeError because Python still passes the instance.
'''