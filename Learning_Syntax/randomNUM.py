# random number generation / cards game
import random

def run():
    low = 1 
    high = 100
    options = ("rock","paper","scissors")
    card = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    # number = random.randint(1, 20)
    number = random.randint(low, high)
    ranNUM = random.random()
    option = random.choice(options)
    random.shuffle(card) # how does this reassign the shuffle values to cards?
    ''' The reason the shuffle method is different from the other methods is because
    the other methods return a fresh value(a new int, float, or element)
    instead,  random shuffle modifies the 'list' you give it in place and
    deliberately returns 'NONE', so if you do assign it to a variable the
    variable will hold the value None '''
    
    # Example of what was explained above about variable assignment with shuffle
    assignedCards = random.shuffle(card)
    print(assignedCards)
    


    print(number)
    print(ranNUM)
    print(option)
    print(card)
