# Num Pad Exercise
def run():
    num_pad = ( (1, 2, 3), 
                (4, 5, 6),
                (7, 8, 9),
                ("*", 0, "#"))

    for row in num_pad:
        for num in row:
            print(num, end =" ") 
            '''prints every number in each row, w/ a space 
                after each number printed''' # This isn't actually a commend
                # python treats it as a string literally which parses, then discards
        print()
