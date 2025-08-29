# conditional expresssions = A one-line shortctut for the if-else statment (ternary operator)
#                            Print or assign one fo two values based ona condition
#                            X if condition else Y

def run():
    num = int(input("Please enter an number: "))
    print("Positive" if num > 0 else "Negative")

    result = "EVEN" if num % 2 == 0 else "ODD"
    print(result) 

    a = 6
    b = 9
    age = 18
    temperature = 30
    user_role = "ADMIN"

    max_num = a if a > b else b
    min_num = a if a < b else b

    status = "Adult" if age >= 18 else "Child"

    weather = "HOT" if temperature > 20 else "COLD"

    access_level = "Full Access" if user_role == "admin" else "Limited Access"

    print(weather)

    print(status)

    print(access_level)