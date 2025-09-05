# Hangman in Python
import random

def run():
    words = ("apple", "orange", "banana", "coconut", "pineapple") # Tuple


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


    def display_loss(wrong_guesses, answer, is_running):
        display_man(wrong_guesses)
        display_answer(answer)
        print("You're out of Guesses")
        print()
        print("o o")
        print(".-.")
        print()
        print("YOU LOSE")
        is_running = False
        return is_running

    def display_hint(hint):
        print(" ".join(hint)) # now including a space between each of the literals in the list

    def display_answer(answer):
        print(" ".join(answer))

    def main():
        answer = random.choice(words) # will select a random word from our tuple
        hint = ["_"] * len(answer) # - ["_"]: is a list literal with one element, the string "_". so your multipling the list by 'len(answer)' times which is Legal
        
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
        guessed_letters = set() # EMPTY SET - in python you normally can't create an empty set with just '()' you need to invoke the set function 'set()'
        is_running = True

        while is_running:
            display_man(wrong_guesses) # 1. Display game board
            display_hint(hint) # 2. Display the word count / hidden word
            guess = input("Guess a letter: ").lower() # 3. Guess a letter

            ### input validation
            ## 1. So user can only insert 1 character rather than a whole string
            if len(guess) != 1 or not guess.isalpha(): # isalpha() only returns true if the value is purely alphabetical letters
                print("Invalid input")
                # if wrong_guesses >= len(hangman_art) - 1:
                    # is_running = display_loss(wrong_guesses, answer, is_running) 
                continue  
            
            ## 2. If we already entered that letter, to avoid repeats
            if guess in guessed_letters:
                print(f"{guess} was already entered")
                # if wrong_guesses >= len(hangman_art) - 1:
                    # is_running = display_loss(wrong_guesses, answer, is_running)     
   
            ###

            guessed_letters.add(guess) # modifying the set by adding letters to it from guess input


            if guess in answer: # This logic checks if our guess in our answer, IMPORTANT "in" is a built-in operator in Python that checks membership, its similar to in 'answer.contains(guess)' in Java
                for i in range(len(answer)): # If the guess is in our answer, it iterates through our word to determine where the letter.
                    if answer[i] == guess: # checking if your guess matches the answer at the exact index we are iterating through.
                        hint[i] = guess # then it replaces the list literal for that specific index with our guess.
            else:
                wrong_guesses += 1
                # if wrong_guesses >= len(hangman_art) - 1:
                    # is_running = display_loss(wrong_guesses, answer, is_running)       

            if "_" not in hint:
                display_man(wrong_guesses)
                print("YOU WIN!")
                is_running = False
            
            elif wrong_guesses >= len(hangman_art) - 1:
                is_running = display_loss(wrong_guesses, answer, is_running)  


            

    main()

if __name__ == '__main__':
    run()

