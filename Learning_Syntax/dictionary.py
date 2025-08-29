# dictionary = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

def run():
    # Today we will do a dictionary of {Country : and Capital}
    capitals = {"U.S.A" : "Washington D.C",
                "India" : "New Delhi",
                "China" : "Beijing",
                "Russia" : "Moscow"}
    # print(dir(capitals)) # prints all attributes methods of a dictionary
    # print(help(capitals)) # prints all attributes methods of a dictionary


    print(capitals.get("U.S.A"))
    print(capitals.get("India")) # Returns value, if key exists
    print(capitals.get("Japan")) # Returns none if country / key doesn't exist
    print(capitals.key("China")) # Returns the key rather than value like above
    print()

    if capitals.get("Russia"): # Since Russia exists it returns true
        print("That capital exists")
    else:
        print("That capital doesn't exist")

    if capitals.get("Japan"): # Since Japan isnt in the list it doesn't exist
        print("That capital exists")
    else:
        print("That capital doesn't exist")
    print()

    capitals.update({"Germany": "Berlin"}) # adds germany to end/bottom of dictionary
    capitals.update({"India": "Mumbai"}) # replaces capital / :value of India Key
    capitals.pop("China") # removes key item from dictionary
    capitals.popitem() # default removes most recent/last key in dictionary
    # capitals.clear() # clears dictionary / removes all keys
    
    keys = capitals.keys()
    for key in capitals.keys():
        print(key)
    print()

    values = capitals.values()
    for value in values:
        print(value)
    print()

    items = capitals.items()
    # print(items)
    for key, value in capitals.items(): # two counters: key and value
        print(f"{key}: {value}")


