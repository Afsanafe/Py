# Python Banking Program

def run():
    
    def show_balance(balance):
        print("***************")
        print(f"Your balance is: ${balance:.2f}")
        print("***************")

    def deposit(balance):
        amount = float(input("Enter an amount you would like to deposit: "))
        if amount < 0:
            print("That's not a valid amount")
            return 0.0
        else:
            return amount

    def withdraw(balance):
        amount = float(input("Enter an amount you would like to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Please withdraw less")
            return 0.0
        elif amount < 0:
            print("That is not a valid amount")
            return 0.0
        else:
            return amount

    def main():
        balance = 0
        is_running = True

        while is_running: # everything under is_running is the body of loop, its just calling the other functions outside of the loop for the functionality - basically using modules
            print("WELCOME TO BANKING PROGRAM")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice (1-4): ") )
            print()

            match choice:
                case 1:
                    show_balance(balance)
                case 2:
                    balance += deposit(balance)
                case 3: 
                    balance -= withdraw(balance)
                case 4:
                    is_running = False
                case _:
                    print("That is not a valid choice")
            print()
        
        print()
        print("Thank you for banking with us, have a nice day!")
    
    if __name__ == '__main__':
        main()
        # balance = 0   # this would make the variable a module-global name, but that block only run when the file is executed as a script.
                        #  if someone imports this module and calls the function, balance wont exist.
        
        
