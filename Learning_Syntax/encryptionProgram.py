# Encryption Program
import random
import string # We will be using some constants from the string module, rather than typing in the characters ourself



def run():
    chars = " " + string.punctuation + string.digits + string.ascii_letters # constants: punctuation, digits, ascii_letters, 
    # print(chars) # will print them all in order
    chars = list(chars) # Before chars was basically a variable of strings, which is why it outputted one continguous string, BUT NOW its a list (type)
                        #   So list(chars) turns "ab" into ['a', 'b'], and print then shows that literal-style view where the each character has single quotes, and commas between each other
    
    key = chars.copy() # we make a copy, SO 'chars' will display the original message, while 'key', which is a clone of 'chars', will be encrypted, and display that new encrypted messages (shuffled)

    random.shuffle(key) # this mixes up the combination of elements in the list, basically every character in order, has an equivalent character in the shuffle, so if their places match, that character you see in key is what's replacing the character in our string

    # Hide this to avoid seeing which characters are associated to which in the new shuffled combination
    # print(f"chars: {chars}")
    # print(f"key: {key}")

        #ENCRYPT

    plain_text = input("Enter a message to ENCRYPT: ")
    cipher_text = ""

    for letter in plain_text: # this will iterate through each character in our string we inputted to 'plain_text'
        index = chars.index(letter) # the index(letter) method returns the position of the first match between our 'plain_text' character and 'chars' character, this position will tell which value to pass in from our 'keys' variable later
        cipher_text += key[index]

    
    print(f"original message: {plain_text}")
    print(f"encrypted message: {cipher_text}")


        #DECRYPT
    cipher_text = input("Enter a message to DECRYPT: ")
    plain_text = ""


    for letter in cipher_text: # this will iterate through each character in our string we inputted to 'plain_text'
        index = key.index(letter) # the index(letter) method returns the position of the first match between our 'plain_text' character and 'chars' character, this position will tell which value to pass in from our 'keys' variable later
        plain_text += chars[index]

    

    print(f"encrypted message: {cipher_text}")
    print(f"decrypted message: {plain_text}")
