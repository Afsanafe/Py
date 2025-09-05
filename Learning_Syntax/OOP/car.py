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