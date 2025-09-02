# Membership Operators = used to test whether a value or variable is found in a sequence 
#                                           (string, list, tuple, set, or dictionary) - included but not limited to
#                                           1. in
#                                           2. not 
# There are two membership operators in Python:
# in → returns True if the value is found.
# not in → returns True if the value is not found.
#
# 🔹 Syntax
# element in collection
# element not in collection
#

def run():
    # word = "APPLE"

    # letter = input("Guess a letter in the secret word: ")
    # letter = letter.upper()


    # if letter in word:
    #     print(f"There is a {letter}")
    # else:
    #     print(f"{letter} was not found")

    # # OR
    # #
    # # if letter not in word:
    # #     print(f"{letter} was not found")
    # # else:
    # #     print(f"There is a {letter}")

    # # Lists, Tuples and Sets will behave similarly

    # students = {"Spongebob", "Patrick", "Sandy"}

    # student = input("Enter the name of a student: ")

    # if student in students:
    #     print(f"{student} is a student")
    # else:
    #     print(f"{student} is not a student")

    # grades = {"Sandy": "A", "Squidward": "B", "Patrick": "F"}

    # student = input("Enter the name of a student: ")

    # if student in grades:
    #     print(f"{student}'s grade is {grades[student]}")
    # else:
    #     print(f"{student} was not found")
    email = "example@example.com"
    # email = "exampleexample.com" # not valid example - test

    if "@" in email and "." in email:
        print("Valid email address")
    else:
        print("Invalid email address")