# Hangman in Python

def run():
    words = ("apple", "orange", "banana", "coconut", "pineapple")


    #dictionary of key:()
    handman_art = {0: ("   ",
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
    
    print(handman_art[0])

