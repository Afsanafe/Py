# logical operators = evaluate multiple conditions (or, and, not)
#                       or = at least one condition must be True
#                       and = both conditions must be True
#                       not = inverts the condition (not False, not True)

def run():
    temp = int(input("Whats the weather outside? "))

    is_raining = False
    if temp > 35 or temp < 0 or is_raining:
        print("the outdoor event is cancelled")
    else:
        print("The outdoor event is still scheduled")

    # is_sunny = bool(input("Is it Sunny?(True or False): "))
    # For bool this doesn't workas input() always returns a string, so any string is turned to True
    #  ...Only empty string is False,  " " == False

    #Correct way to do it
    val = input("Is it Sunny?(True or False): ")
    is_sunny = val == "True" # compare strings val and "True", store Boolean in 'is_sunny'
    ###            == comparison operator returns boolean value

    print(type(is_sunny))
    print(is_sunny)
    if temp >= 28 and is_sunny == True:
        print("It is HOT outside")
        print("It is SUNNY")
    elif temp <= 0 and is_sunny:
        print("It is COLD outside")
        print("It is sunny")
    elif 28 > temp > 0 and is_sunny:
        print("It is WARM outside")
        print("It is CLOUDY")
        
        

    if temp >= 28 and not is_sunny:
        print("It is HOT outside")
        print("It is NOT SUNNY")
    elif temp <= 0 and not is_sunny: #### not, inverts the condition
        print("It is COLD outside")
        print("It is NOT sunny")
    elif 28 > temp > 0 and not is_sunny:
        print("It is WARM outside")
        print("It is CLOUDY")

    
    



    