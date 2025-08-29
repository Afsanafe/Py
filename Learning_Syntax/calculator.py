# Python Calculator

def run():
    operator = input("Enter an operator (+ - * /): ")
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

    if operator == "+":
        result = num1 + num2
        print(result)

    elif operator == "-":
        result = num1 - num2
        print(result)
        
    elif operator == "*":
        result = num1 * num2
        print(result)

    elif operator == "/":
        result = num1 / num2
        print(result)

    elif operator == "^":
        pass # Nothing happens, quite literally a place holder for code