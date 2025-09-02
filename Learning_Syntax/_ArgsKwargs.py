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
    
    print(add(1, 2, 3, 4, 5)) # it doesn't matter how many arguments you pass, it will add them all up | BUT if you are using both args and kwargs, ORDER DOES MATTER
    # Remember the argument passed in a function is always a tuple

    def display_name(*args):
        for args in args:
            print(args, end=" ")
    display_name("Dr.", "Spongebob", "Squarepants", "III")
    print()

    def print_address(**kwarfs):
        print(type(kwarfs)) # kwargs is a dictionary
        for key, value in kwarfs.items():
            print(f"{key}: {value}") # or print(f"{key} : {kwarfs[key]}")



    print_address(street="123 Fake St.", 
                  city="Coolsville", 
                  state="MA", 
                  zip="01902")
    # *args collects all extra positional arguments into a tuple 
    # **kwargs collects all extra KEYWORD arguments into a dict 

    # And it is the appropriate unpacking operators which calls the necessary python function call semantic to make the argument into Either a TUPLE CONTAINER or DICT CONTAINER

    # So the rule is:

    # * in the parameter list → “collect the rest of the positionals into a tuple.”

    # ** in the parameter list → “collect the rest of the keywords into a dict.”

    # Similarly, on the call side:

    # f(*mylist) unpacks an iterable into positional arguments.

    # f(**mydict) unpacks a mapping into keyword arguments.

    # For dictionarys, if statments can only check the key arguments, you can only get the values associated with they key with the .get() method
    
    def _attempt1_(*args, **kwarfs):
        for arg in args:
            print(arg, end="")
        if "class2" in kwarfs:
            print()
            print(f"You have class today!")
            print()
        for key,value in kwarfs.items():
            print(f"You have {key} which is {value}")
            print()

        for chicken, soupo in kwarfs.items(): # key, value are just naming conventions, the the variable names are arbitrary
            print(f"You have {chicken} which is {soupo}")
            print()
        # Python knows that .items() returns tuples of (key, value) for each item in the dictionary, so it unpacks each tuple into the two variables you provide.


    _attempt1_(3, "Math", 5, 7, 2, "English", class1="Operating Systems", class2="Intro to C Security", class3 ="GUI", class5="Prob & Stats")



    # add(1,2,3) # why does this become a tuple? because *args packs the arguments into a tuple
    # print(add (1,2))
    # print(add(1,2,3))

    # .get(key) retrieves the value for a specific key from the dictionary.
    # .keys() returns a view of all the keys in the dictionary.
    # .items() returns a view of key-value pairs (tuples) in the dictionary, allowing you to iterate over both the key and its associated value.






