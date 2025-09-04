# Hangman in Python
import random

def run():
    words = ("apple", "orange", "banana", "coconut", "pineapple")


    #dictionary of key:()
    hangman_art = {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\ ", # in python to represent one backslash '\' you need to include two of the backslashes, as one is essentially an escape in python
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}
    
    def display_man(wrong_guesses):
        print("=============================")
        for line in hangman_art[wrong_guesses]:
            print(line)
        print("=============================")

    def display_hint(hint):
        print(" ".join(hint)) # now including a space between each of the literals in the list

    def display_answer(answer):
        print(" ".join(answer))

    def main():
        answer = random.choice(words) # will select a random word from our list
        hint = ["_"] * len(answer) # - ["_"]: is a list literal with one element, the string "_". so your multipling the list by 'len(answer)' times
        
        '''
            ? What's a “list literal” ?
        A list literal is just the bracket notation that directly creates a list:
         - [] → empty list
         - ["_"] → a list with one element, the string "_"
         - [1, 2, 3] → a list with three integers
        “Literal” means you're writing the value itself in code, not computing it.

            ? How can you “multiply” a list or string by an int ?
        In Python, the * operator is overloaded for sequences (strings, lists, tuples).
        sequence * n (or n * sequence) means repeat/concatenate the sequence n times.



        You can multiply a string/list by an int (order doesn't matter: 5 * "_" works too), but not by another string: "_" * "5" → TypeError.
        '''
        wrong_guesses = 0
        guessed_letters = set() # in python you normally can't create an empty set with just '()' you need to invoke the set function 'set()'
        is_running = True

        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            display_answer(answer)
            
            guess = input("Guess a letter: ").lower()

            ### input validation
            ## 1. So user can only insert 1 character rather than a whole string
            if len(guess) != 1 or not guess.isalpha(): # isalpha() only returns true if the value is purely alphabetical letters
                print("Invalid input")
                continue

            ## 2. If we already entered that letter, to avoid repeats
            if guess in guessed_letters:
                print(f"{guess} was already entered")
                continue

            guessed_letters.add(guess)


            if guess in answer: # This logic checks if our guess in our answer, IMPORTANT "in" is a built-in operator in Python that checks membership, its similar to in 'answer.contains(guess)' in Java
                for i in range(len(answer)): # If the guess is in our answer, it iterates through our word to determine where the letter.
                    if answer[i] == guess: # checking if your guess matches the answer at the exact index we are iterating through.
                        hint[i] = guess # then it replaces the list literal for that specific index with our guess.
            else:
                wrong_guesses += 1


            # display_answer(answer)


    main()

    if __name__ == '__main__':
        run()

