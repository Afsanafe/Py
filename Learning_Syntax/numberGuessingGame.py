# Python number guessing game
import random

def run():

    lowest_num = 1
    highest_num = 100
    answer = random.randint(lowest_num, highest_num)

    print(answer)
    guesses = 0
    is_running = True

    print("Python Number Guessing Game")
    print(f"Select a number between {lowest_num} and {highest_num}")

    while is_running: # because 'is_running' is a boolean you don't have to write 'while is_running = True'
        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            guesses += 1
            if guess < lowest_num or guess > highest_num:
                print("That number is out of range")
                print(f"Please select a number between {lowest_num} and {highest_num}")
            elif guess < answer:
                print("Too Low! Guess Again.")
            elif guess > answer:
                print("Too High! Guess Again")
            elif guess == answer:
                print("Correct! you guessed correctly.")
                print(f"Just took you {guesses} guesses")
                is_running = False
                break
        else:
            print("Invalid Guess")
            print(f"Please select a number between {lowest_num} and {highest_num}")
