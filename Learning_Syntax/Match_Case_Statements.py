# Match-case statement (switch): An alternative to using many 'elif' statments
#                               Execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable
def run():
    def is_weekend(day):
        match day:
            case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                return False
            case "Saturday" | "Sunday":
                return True
            case _: # underscore case is the default case
                return "Invalid day"

    print(is_weekend("Monday"))
    print(is_weekend("Friday"))
    print(is_weekend("Sunday"))
    print(is_weekend("chicken"))