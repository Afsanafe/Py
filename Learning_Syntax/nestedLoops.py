# Nested loops: A loop within another loop(outer, inner)
#               outer loop:
#                   inner loop:

def run():

    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns you would like: "))
    symbol = input("Enter a symbol to use: ")
    for x in range(rows):
        for y in range(columns):
            print(symbol, end=" ") # end="\n", is the same as \n, thats how you write python newline
        print() # This basically prints a newline, because print outputs newline by default