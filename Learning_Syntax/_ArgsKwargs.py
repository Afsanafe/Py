# *args and **kwargs are used to pass a variable number of arguments to a function.
# 
# *args allows you to pass a variable number of non-keyword arguments to a function.
# **kwargs allows you to pass a variable number of keyword arguments (i.e., named arguments) to a function.
#
# *args  = allows you to pass multiple non-key arguments, you put this in a tuple
# **kwargs = allows you to pass multiple keyword arguments (i.e., named arguments), you put this in a dictionary
#           * unpacking operator, this represents extra positional arguments as a tuple
#           ** double unpacking operator, this represents extra keyword arguments as a dictionary

#           often used in function definitions to handle variable numbers of arguments
#           1. positional 2. default 3. keyword 4. ARBITRARY

def run(): 
    def add(*args): # we are going to iterate over args, because we don't know how many arguments will be passed
        print(type(args))
        total = 0
        for arg in args:
            total += arg
        return total
    
    print(add(1, 2, 3, 4, 5)) # it doesn't matter how many arguments you pass, it will add them all up
    # Remeber the argument passed in a function is always a tuple

    def display_name(*args):
        for args in args:
            print(args, end=" ")
    display_name("Dr.", "Spongebob", "Squarepants", "III")
    print()

    def print_address(**kwarfs):
        print(type(kwarfs)) # kwargs is a dictionary
        for key, value in kwarfs.keys():
            print(f"{key}: {value}") # or print(f"{key} : {kwarfs[key]}")



    print_address(street="123 Fake St.", 
                  city="Coolsville", 
                  state="MA", 
                  zip="01902")
    



    # add(1,2,3) # why does this become a tuple? because *args packs the arguments into a tuple
    # print(add (1,2))
    # print(add(1,2,3))





