# iterables = an object/collection that can return its elements one at a time,
#              permitting it to be iterated over in a for-loop.
#              And allowing you to traverse through all the elements without exposing the underlying structure.
# Examples of iterables: lists, strings, dictionaries, sets, tuples, files, generators, etc.

def run():
    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        print(number, end =" - ")
    print()

    # sets can't be reversed

    name = "Alicia Keys"

    for character in name:
        print(character, end =" - ")
    print()
   
    name = "Draco Malfoy"

    # Iterate every 2 characters
    for i in range(0, len(name), 2):
        print(name[i:i+2], end=" - ") # [0:2] prints indices 0 and 1
                                    # [2:4] prints indices 2 and 3
                                    # [4:6] prints indices 4 and 5
                                    # [6:8] prints indices 6 and 7
                                    # [2:5] prints indices 2, 3, and 4
    print()

    my_dictionary = {"A": 1, "B": 2, "C": 3}
    
    for key in my_dictionary:
        print(key)

    for key, value in my_dictionary.items():
        print(f"{key}: {value}")