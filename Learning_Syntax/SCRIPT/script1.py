# from script2 import *

# print(dir()) # you should see afsanafe@Afsas-MacBook-Pro-2 SCRIPT % python script1.py
# # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# # focus on seeing dunder name (__name__)

# print(__name__) # this will output '__main__'

# if __name__ == '__main__' # this is why we create an if statement dunder name equals the string dunder main
print(__name__) # __name__ is a special built-in variable in every Python module
'''
With the import you will see first script2 run, and it will output
script2's file name which is just 'script2'

And then

it will run the print for dunder name in this file which is just 
dunder main '__main__'

Things to note is:

    - If you run a file directly, say in script1.py, which is the file you are executing/running
    Python sets __name__ to "__main__" in that file
    - If you import the file as a module so (in myscript1, you do "import mysScript2")
    then Python sets __name__ to the modules name which in this case would be
    "Script1"
'''