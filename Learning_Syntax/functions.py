# function = A block of reusable code
#            place () after the function name to invoke it

def run():
    print("Happy birthday to you!") # Say you wanted to say this 3 times,
    print("You are old!")           # You could print it out in 3 bundles
    print("Happy birthday to you")  # Or just create a function and invoke -
    print("")                       # - 3 times


    def happy_birthday():
        print("Happy Birthday to you!")
        print("You are old!")    
        print("Happy birthday to you")
        print("")    

    def happy_birthday_name(name): # Overloading is not supported Natively on Python
        print(f"Happy Birthday to {name}!") # Only supported on C / C++
        print("You are old!")    
        print("Happy birthday to you")
        print("")       
    
    happy_birthday() #1. calls / invokes function
    
    #2. you can also send arguments / data within the parenthesis
    happy_birthday_name("Joe") # 2b. You are sending in Joe as an argument
    #2c. You need a matching set of parameters in a function, ORDER MATTERS

    
# return = statement used to end a function
#          and send a result to the caller
    def add(x, y):
        z = x + y
        return z
    
    def subtract(x, y):
        z = x - y
        return z
    
    def multiply(x, y):
        z = x * y
        return z
    
    def divide(x, y):
        z = x / y
        return z
    
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))

    print()

    def create_name(first, last):
        first = first.capitalize()
        last = last.capitalize()
        return first + " " + last 
    
    full_name = create_name("spongebob", "squarepants") # invoke argument
                                                        # store return data in variable

    print(full_name) # use variable stored with data for print function
