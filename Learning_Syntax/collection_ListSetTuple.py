# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FSTER

def run():
    ####################################################################################
    '''List[]'''
    """ Ordered: items have a defined order (index starts at 0) """
    """ Mutable: You can add, remove, or change items """
    """ Allows duplicates """
    """ Can store mixed data types """
    ####################################################################################
    print("############################") 
    print("'''List[[]]'''")
    print("############################") 

    fruit = "apple"

    fruits = ["apple", "orange", "banana", "coconut", 6, True] # List



    print(fruit)
    print(fruits) # prints the entire list
    print(fruits[2]) # prints a specific item in the list, in this case : banana
    print(fruits[:3]) # this prints the first to third elements
    print(fruits[::2]) # this prints every other element starting index 0
    print(fruits[::-1]) # this prints all the elements in reverse order
    ''' you can use the index operator with collections 
            much like you can use with strings '''
    print()

    '''Another cool thing you can do with collections
    is iterate over them with for loops  '''

    for x in fruits:
        print(x)


    ###########
    # print(dir(fruits)) # prints all attributes
    # print(help(fruits)) # prints what each method does

    print(len(fruits)) # returns number of items in list 
    print("pineapple" in fruits) # finds in an item is within 
    fruits[3] = "pineapple" # you can use indexes to reassign values

    fruits.remove("apple")
    fruits.insert(0, "pineapple")
    fruits.insert(3, "pineapple")
    fruits.append("orange") # adds orange to list
    # fruits.sort()
    print(fruits)
    fruits.reverse() # reversed in index order
    
    # reverse alphabetical order
    # fruits.sort()
    fruits.reverse
    print(fruits)

    print(fruits.index("orange")) # returns index of listed element

    print(fruits.count("pineapple")) # returns the number of times item is found in list



    ####################################################################################
    '''Set{}'''
    """ Unordered: No guarantee of order """
    """ Mutable: You can add, remove """
    """ No duplicates allowed """
    """ Only hashable (immutable) elements allowed """
    ####################################################################################
    print("############################") 
    print("'''Set{{}}'''")
    print("############################") 
    print()

    setofFruits = {"apple", "orange", "banana", "coconut", "coconut"}
    print()
    a = {7, 1, 2, 3}
    b = {3, 4, 5}
    print(a.union(b)) # union orders
    print(a.intersection(b))
    print(a.difference(b)) # which values of variable a is variable b missing
    print(b.difference(a)) # which values of variable b is variable a missing
    print()
    


    ####################################################################################
    '''Tuple()'''
    """ Ordered: Like lists, elements have a fixed order """
    """ Cannot change, add, or remove items """
    """ Allows duplicates """
    """ Can store mixed data types """
    """ Slight faster and memory-efficient than lists """

    ####################################################################################
    print("############################") 
    print("'''Tuple(())'''")
    print("############################") 

    fruitTuple = ("apple", "orange", "banana", "coconut", "coconut")
    print(len(fruitTuple))
    print("pineapple" in fruits)
    print(fruits.index("banana"))
    print(fruits.count("coconut"))

    my_tuple = (9,2,3)
    my_single_item = (11,)

    p = my_tuple[0]

    for fruitz in fruitTuple:
        print(fruitz)

    print()
    print(p)
    print(my_single_item[0])
    


''' They all pretty much share the same functions/methods but they don't share all
methods '''