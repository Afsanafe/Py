# Slot Machine Application
import random


def run():
    def spin_row():
        symbols = ['#', '*', '_', '+', '&']
        
        # OPTION A:
        # results = [] # list comprehension broken down : empty list
        # for symbol in range(3): # loop 3 times, because we want 3 slot positions
        #     results.append(random.choice(symbols)) # telling the random object to randomly CHOOSE a symbol from our list of symbols, then append that to our EMPTY LIST (results)
        
        # OPTION B:
        return [random.choice(symbols) for _ in range(3)] # List comprehension: runs "random.choice(symbols)" three times and collects the results in a list 
                                                          # '_': this is a 'throwaway' variable name. Its a normal variable, but by convention it means "I dont use this value." We just need a variable to satisfy the for syntax, but we never read it
    


    def display_row(row):
        print("**************")
        print(" | ".join(row)) # we are taking our iterable and joining each element with a space  ....  " | ".join(row) builds one new string by concatenating the items of row with " | " between them. It doesn’t print anything by itself and it doesn’t modify the list.
        print("**************")

        # Conceptually, it’s like:
        # s = ""
        # first = True
        # for x in row:            # assumes x is a str
        #     if not first:
        #         s += " | "
        #     s += x
        #     first = False
        # print(s)


    def get_payout(row, bet): # function will calculate payout
        if row[0] == row[1] == row[2]:
            if row[0] == '#':
                return bet * 2
            elif row[0] == '*':
                return bet * 150
            elif row[0] == '_':
                return bet * 10
            elif row[0] == '+':
                return bet * 50
            elif row[0] == '&':
                return bet * 10000
        return 0

    def main():  
        balance = 100

        print("***********************")
        print("Welcome to Python Slots")
        print("Symbols: # * _ + &")
        print("***********************")

        while balance > 0:
            print(f"Current balance: ${balance}")

            bet = (input("Place your bet amount: "))


            if not bet.isdigit(): # this condition passes if every character of the variable bet is NOT an int/digit
                print("Please enter a valid number")
                continue # affects only the inner most loops and skips for this one specific condition that passes, inner loop WILL CONTINUE to run for remainder of the body whilst the while loop condition is true.
                            # the keyword 'break' would only cause the code to exit the entire 'while loop'
                


            bet = int(bet)

            if bet > balance:
                print()
                print("Insufficient funds")
                print()
                continue

            if bet <=0:
                print("Bet must be greater than 0")
                continue

            balance -= bet

            row = spin_row()

            print("Spinning...\n")
            display_row(row)

            payout = get_payout(row, bet)

            if payout > 0:
                print(f"You won #{payout} !")
            else:
                print("Sorry no match :(, Don't give up Tho!)")
            
            balance += payout

            play_again = input("Do you want to keep going? (Y/N)").upper()
            

            if play_again != 'Y':
                break

    main()


if __name__ == '__main__': # the reason __name__ was created so you can know when a file is being run standalone VS when its being run as an imported module, as this only runs when you execute it as a standalone script
    run() # and also properly defines the entry point to the program where you want it to, regardless of the function order.