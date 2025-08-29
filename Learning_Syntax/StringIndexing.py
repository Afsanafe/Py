# indexing = accessing elements of a sequence using [] (indexing operator)
#               [start : end : step]

def run():
    credit_number = "1234-5678-9012-3456"
    
    print(credit_number[0])
    credit_number[0:4]
    print(credit_number[0:4]) # [starting index : ending index] -> prints characters from index 0 to 4

    print(credit_number[5:9])

    print(credit_number[5:]) # python assumes we want everything from the 5th index and after by omitting our end value

    print(credit_number[-1]) # negative index numbers, basically go the reverse order of the string
    
    print(credit_number[::2]) # Step of '2', makes us print every 2 characters starting with index[0] character,
                              #     ... so it will first out the first character, then proceed with the 'step' pattern/rule

    print(credit_number[::3]) # prints the first character, then every 3rd index of the string

    # exercise: Print last 4 digits
    last_digits = credit_number[-4:] # starts at 4 to last element, then prints last remaining digits
    print(last_digits)

    # exercise: reverse string
    new_credit_number = credit_number[::-1] # To reverse a string, you just reverse the "step" value
                                                # ... with a negative value i.e. '-1'
    print(new_credit_number)