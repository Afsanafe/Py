# module = a file containing a code you want to include in your program
#               use 'import' to include a module (built-in or your own)
#               useful to break up a large program reusable separate files

#import math  # built-in module

import math as m # referring to our module as an alias

# print(math.pi) # before with just 'import math'
def run():
    print(m.pi) # now with alias

    print(m.sqrt(25))
