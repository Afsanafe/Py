# Concession Stand Program (Exercise)

def run():
    menu = {"pizza" : 3.00,
            "nachos" : 4.50,
            "popcorn" : 6.00,
            "fries" : 2.50,
            "chips" : 1.00,
            "pretzel" : 3.50,
            "soda" : 3.00,
            "lemonade" : 4.25} # dictionary,  8 keys
    cart = []
    total = 0

    print("------------- MENU -------------")

    for key, value in menu.items(): # This loop is known as TUPLE UNPACKING 
        print(f"{key:10}: ${value:.2f}") # formats every key to have 10 spaces, and every value to have 2 decimals
    print("--------------------------------")

    while True: # whats the conditional parameter, what needs to be True?
        food = input("Select an item (q to quit): ").lower() #
        if food == 'q':
            break # exit this loop
        # elif menu.get(food) # returns none
        elif food in menu:
            cart.append(food)
            print(f"{food} : ADDED TO CART")
        else:
            print("Try again")
    
    print("--------------------------------")
    print("------------- ORDER ------------")
    print("--------------------------------")
    for food in cart:
        total += menu.get(food) # .get() returns value, which is why we were able to do arithmetic
        print(food, end=" ")
    print()
    print(f"Total is ${total:.2f}")
    # print(cart)