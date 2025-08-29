### Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

def run():
    username = input("Enter a username: ")

    if (len(username) > 12):
        print("Error: Your username is more than 12 characters")

    elif (username.count(" ") > 0):
        print("Error: Your username contains a space")

    elif (username.isalpha() != True): # boolean must be: True, not true, its cap sensitive
    # Technically isalpha() would also check for spaces as well since only letters are allowed
        print("Error: your username contains a digit")
    else: 
        print(f"Welcome {username}!")


        ##### Alternative #######
        # if len(username) > 12:
        #     print("Error: Your username is more than 12 characters")

        # elif not username.find(" ") == -1: # if it doesn't find any space it returns -1, but the condition is NOT,
        #                                     # ... so the opposite meaning if it returns anything BUT -1.
        #     print("Error: Your username contains a space")

        # elif not username.isalpha(): # Since conditions default to true on their, not true is the opposite
        #     print("Error: your username contains a digit")
        # else: 
        # print(f"Welcome {username}!")