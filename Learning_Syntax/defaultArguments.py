# Default Arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces number of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary
import time 

def run():
    # def net_price(list_price, discount, tax): # 
    #     return list_price * (1- discount) * (1 + tax)


    # Why are the default values and the values passed in by the invocations in the print functions in the bottom treated as integers rather than strings
    def net_price(list_price, discount = 0, tax = 0.05): # Here we are setting default arguments in the parameters
        return list_price * (1- discount) * (1 + tax)

    

    # print(net_price) # this doesn't print properly because theres no variable named net_price that you are passing into the print function
                       # You aren't invoking the function - you need () paranthesis

    print(net_price(500, 0, 0.05))
    print(net_price(500, 0.1, 0))
    print(net_price(500, 0.05))
    print(net_price(500, 0))
    print(net_price(500))

    def count(end, start = 0):
        for x in range(start, end+1):    
            print(x)
            time.sleep(1) # pauses the execution of the current program for 1 second
            # time.sleep(0.5) # pauses the execution of the current program for 1/2 second
        print("DONE!")

    count(15)

