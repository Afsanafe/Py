    # Input() = A function that prompts users to enter data
#           Returns that data as a string


def run():
    name = input("What is your name?: ")

    age = input("How old are you?: ")

    age = int(age) # since all inputs are strings, you need to typecast to integer or float for arithmetic
    age += 1
    print(f"Hello {name}")
    print(f"You are {age} years old - 1")


    age = int(input("What is your actual age?: "))


    ## Exercise 1 Rectangle Area Calc

    length = float(input("What is the length of your rectangle?: "))
    width = float(input("What is the width of your rectangle?: "))

    print(f"Your rectangle's area is {length * width} ㎡")


    # Exercise 2 Shopping Cart Program

    item = input("What item would you like to buy?: ")
    price = float(input("What is the price?: "))
    quantity = int(input("How many would you like?: "))
    total = price * quantity

    print(f"You have bought {quantity} x {item}/s")
    print(f"Your total is {total}")
