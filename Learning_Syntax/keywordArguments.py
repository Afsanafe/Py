# Keyword Arguments = an argument preceded by an identifier
#                     helps with readability
#                     ORDER of Arguments DOES NOT Matter
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


def run():
    def hello(greeting, title, first, last):
        print(f"{greeting} {title}{first} {last}")
    
    hello("Hello", "Mr.", "Spongebob", "Squarepants") # This would output "Hello Mr.Spongebob Squarepants"
    hello("Hello", "Spongebob", "Squarepants", "Mr.") # This would output "Hello Mr.Spongebob Squarepants"
    # These invocations print in different orders, because order matters for arguments -- BUT that can be solved with keyword arguments

    # Keyword arguments
    hello(greeting="Hello", title="Spongebob", last="Squarepants", first="Mr.") # Now the order doesn't matter, as keyword arguments specify the arguments

    # Anther example of keyword argument
    for x in range(1, 11):
        print(x, end=" ") # In the print function "end = " is a keyword argument

    print()
    # Another print function keyword argument
    print("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", sep="-") # when you make each value an argument, 'sep=' defines what string to put between multiple print arguments in a print()

    ############
    # EXERCISE #
    ############

    def get_phone(country, area, first, last): # gets the phone number
        return f"{country}-{area}-{first}-{last}"

    phone_num = get_phone(country = 1, area = 123, first = 456, last = 7890)

    print(phone_num) 

    