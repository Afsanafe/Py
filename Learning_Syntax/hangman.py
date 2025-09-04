# Hangman in Python

def run():
    words = ("apple", "orange", "banana", "coconut", "pineapple")


    #dictionary of key:()
    hangman_art = {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\ ", # in python to represent one backslash '\' you need to include two of the backslashes, as one is essentially an escape in python
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}
    
    for line in hangman_art[0]: # in loops, this dictionary is doing a 'dictionary key lookup', NOT an index, so the [...] operator uses the key stored for an exact match, so whatever the key is what you would specifically insert into the operator
        print(line)

