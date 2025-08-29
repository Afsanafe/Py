# Python Rock, Paper, Scissor Game
import random

def run():
    options = ("rock", "paper", "scissor")
    
    play = True

    while play == True:
        player = None # what value is none?
        computer = random.choice(options)
        while player not in options: #### variable not in tuple loop
            player = input("Enter a choice (rock, paper, or scissors): ")
        
        

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        
        if player == computer:
            print("It's a tie")
        elif player == "rock" and computer == "paper":
            print("Paper beats Rock, Computer Wins!")
        elif player == "rock" and computer == "scissor":
            print("Rock beats Scissor, You win!")
        elif player == "paper" and computer == "scissor":
            print("Scissor beats Paper, Computer Wins!")
        elif player == "paper" and computer == "rock":
            print("Paper beats Rock, You win!")
        elif player == "scissor" and computer == "rock":
            print("Rock beats Scissor, Computer wins!")
        elif player == "scissor" and computer == "paper":
            print("Scissor beats Paper, You win!")

        play = bool(input("Do you still wish to play? (Enter yes/no): ").lower())
        if play != "yes":
            play = False

    print("Thanks for Playing!")
    

