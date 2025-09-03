from script1 import * 

## If you were to run the code right now, specifically this file
# it won't output anything do to the condition,
# The condition will fail because __name__ 

def favorite_drink(drink):
    print(f"your favorite drink is {drink}")

def main():
    print("This is script 2")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye")

if __name__ == '__main__':
    main()