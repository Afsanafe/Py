# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) : Local -> Enclosed -> Global -> Built-in

# Local: Variables defined inside the current function.
# Enclosing: Variables in the enclosing (outer) function.
# Global: Variables at the top level of the module.
# Built-in: Python’s built-in names.

from math import e # e is NOT an alias, it refers to math.e, which is eulers constant
# from math import e as Euler   # use the keyword 'as' to alias something to an object

def run():

    # # Enclosed scope
    # def func1(): 
    #     a=1

    #     def func2(): 
    #         print(a) # Prints enclosed scope variable, not local scope, as a in root function/enclosing function
    #     func2()

    # func1()


    # # global scope
    # def func1(): 
    #     print(a)

    # def func2(): 
    #     print(a) # Prints enclosed scope variable, not local scope, as a in root function/enclosing function

    # a = 3 # global variable, accessibly to all functions

    # func1()
    # func2()


    # built-in 
    def func1():
        print(e)
    
    e = 3 # print's global version, as global comes before built-in, in the LEGB scope order
    func1()
