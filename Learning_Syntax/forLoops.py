# for loops = execute a block of code a fixed number of times. 
#           You can iterate over a range, string, sequence, etc
def run():
    # you can iterate over integers or even strings in for loops
    # for variable in range(initial, ending, interval or n++)
    for x in range(1, 11, 3):
        print(x)
    print("Happy New Years")

    for x in range(1,21):
        if x == 13:
            continue # skip number
        else: 
            print(x)
    
    for x in range(1,21):
        if x == 13:
            break # Exit loop
        else: 
            print(x)