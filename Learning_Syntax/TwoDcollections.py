# 2D collections

def run():
    fruits =     ["apple", "orange", "banana", "coconut"]
    vegetables = ["celery", "carrots", "potatoes"]
    meats =      ["chicken", "fish", "turkey"] # This is a 1D  list

    groceries = [fruits, vegetables, meats] # This is 2D list
    
    # Also when defining a 2D list you can omit the 1D lists, and 
    #  directly define the 3D list with the brackets you would like
    numbers = [[1,2,3], [9,7,3], [12, 5, 17]]

    print(groceries[0]) # This returns entire fruits list
    print(groceries[1]) # This returns entire vegetables list
    print(groceries[2]) # This returns entire fruits list
    

    print()
    print(groceries[2][1]) # Row 2, column 1 = meats, fish, so fish is output
    
    print()
    # print(numbers)
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])

    print()
    
    for value in numbers:
        for digit in value:
            print(value, end=" ")
        print()

    # Another way to do it would be:
    fruits2 = ["apple", "orange", "banana", "coconut", "pear", "kiwi"]

    # start at 0, go up to len(fruits) (exclusive), stepping by 2:
    for i in range (0, len(fruits), 2):
        print(f"Index {i} ->", fruits2[i]," of ", fruits2)
    print()

    # Another way to do it:
    # fruits[ start : stop : step]
    # for fruit in fruits2[0:len(fruits2):1]:
    ''' more idiomatically: '''
    for fruit in fruits2[::1]:
        print(fruit)



 