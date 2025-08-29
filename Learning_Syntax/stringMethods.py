# string methods

def run():
    name = input("Enter your full name: ")
    phone_number= input("Enter your phone number: ")

    result = len(name) # len() funciton provides length of string, returns an integer, reads spaces also

    result2 = name.find(" ") # first look into methods, find() method will look for the first occurence of a space " "

    result3 = name.rfind("e") # finds last occurence of a character/string, returns -1 when nothing found

    result4 = name.capitalize() # Only makes first character capital
    
    result5 = name.upper() # makes all letters in string upper case

    result6 = name.lower() # makes all letters in string lower case

    result7 = name.isdigit() # only returns true if string only contains characters of numbers, no combination/no letters return true 

    result8 = name.isalpha() # only returns true if string only contains letters, no combination/any numbers

    result9 = phone_number.count("-") # counts the number of times a certain character is read

    result10 = phone_number.replace(" ", "-") # replaces all of the first specified character with the second specified character

    print(result)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)
    print(result8)
    print(result9)
    print(result10)


 #########   print(help(str)) # will output all string methods !!!!!!!!!!!!!  ########
    print(help(str)) # will output all string methods !!!!!!!!!!!!!