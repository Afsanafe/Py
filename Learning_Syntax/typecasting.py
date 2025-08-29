
    #   Typecasting = the process of converting one variable to another
#                   str(), int(), float(), bool()
def run():
    name = "Bro Code"
    age = 25
    gpa = 3.2
    is_Student = True

    print(type(name)) # gets the type of our 'name' variable, output: <class 'str'>
    print(type(age)) # gets the type of our 'age' variable, output: <class 'int'>
    print(type(gpa)) # gets the type of our 'gpa' variable, output: <class 'float'>
    print(type(is_Student)) # gets the type of our 'is_Student' variable, output: <class 'bool'>

    gpa = int(gpa) # Type casted from float to int
    print(gpa) 

    age = float(age) 
    print(age) # Type caseted from int to float

    age = str(age)
    print(age) # Type casted from float to string
    print(type(age)) # the value '25' becomes a string

    # !THIS IS NOT LEGAL!:
    #   age += 1, you can't increment, because it's now a string

    # THiS IS LEGAL:
    age += "1" # This is string concatentation
    print(age) # Initially after typecast: 25.0 -- After string concat --> 25.01

    name = ""
    name = bool(name)
    print(name) # This will output FALSE because theres nothing in the name variable

    name = "NOM"
    name = bool(name)
    print(name) # This will NOW output TRUE, becauses theres something in the variable

    # User input is always a string, as input() returns the entered data as a string, 
    #  so typecasting is useful in transforming user data from strings if needed.
