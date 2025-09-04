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

    print(f"chars: {chars}")
    print(f"key: {key}")


