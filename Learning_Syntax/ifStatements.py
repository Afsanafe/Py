# If statements

def run():
    # age = int(input("Enter your age: "))
    # if age >= 18:
    #     print("You are now signed up!")
    # elif age < 0:
    #     print("You aren't born yet")
    # elif age > 100:
    #     print("Congrats on your old age")
    # else: 
    #     print("You must be 18+ to sign up")

    response = input("Would you like food? (Y/N): ")

    if response == "Y":
        print("Have some food!")
    elif response == "N":
        print("No food for you!")
    else:
        print("Not a valid input")

    online = True

    if online: ##### only if its true
        print("The user is online")
    else: ###### only if its false
        print("The user is offline")
    