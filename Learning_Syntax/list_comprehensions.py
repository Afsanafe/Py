# List Comprehensions = A concise way to create lists in Python using a single line of code!
#                       Compact and easier to read than traditional loops
#   Formula to follow = [expression for value in iterable if condition]

# expression → the value to put in the list

# value → variable representing each element in the iterable

# iterable → sequence (list, string, range, etc.) to loop through

# condition (optional) → filter elements

def run():
    doubles = []
    for x in range(1,11): # remember in for loops such as this, the second value is exclusive, 
                          # so the range for this loop is 1 to 10, as 11 is NOT Included
        doubles.append(x * 2)
    print(doubles)
    # This is a lot to read, theres a way make this more compact and easier to read.


    ############ Earlier item now turned into a list comprehension ###############

    # doubles_v2 = [expressions for value in iterable if condition]
    doubles_v2 = [x * 2 for x in range(1, 11)]

    triples = [y * 3 for y in range(1,11)]
    squares = [z* 2 for z in range (1, 11)]

    print(doubles_v2)
    print(triples)
    print(squares)

    fruits = ["apples", "bananas", "cherries", "coconuts"]
    fruits = [fruit.upper()for fruit in fruits]

    print(fruits)

    fruits2 = ["apples", "bananas", "cherries", "coconuts"]
    fruits_chars = [fruitz[0] for fruitz in fruits2] # if given one string, you only index a the characters,
                                                     #  but if given a set of strings, you index the strings themselves
    print(fruits_chars)

    numbers = [1, -2, 3, -4, 5, -6]

    positive_nums = [num for num in numbers if num >= 0] # since we aren't doing any different expressions, the expression is just 'num' to return itself
    negative_nums = [num for num in numbers if num < 0] # since we aren't doing any different expressions, the expression is just 'num' to return itself
    even_nums = [ num for num in numbers if num % 2 == 0]
    odd_nums = [ num for num in numbers if num % 2 == 1]

    print(negative_nums)

    grades = [85, 42, 58, 56, 31, 82, 99]
    passing_grades = [grade for grade in grades if grade >= 60]
    print(passing_grades)
