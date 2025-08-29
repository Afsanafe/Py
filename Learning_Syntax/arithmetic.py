# # Arithmetic
def run():
    friends = 5
    print(f"number of friends: {friends}")

    # addition
    friends = friends + 100
    friends += 100
    print(f"number of friends after addition: {friends}")

    friends = friends - 7
    friends -= 7
    print(f"number of friends after subtraction: {friends}")

    friends = friends * 4
    friends *= 4
    print(f"number of friends, after multiplication: {friends}")

    friends = friends / 3
    friends /= 3
    print(f"number of friends, after division: {friends}")

    friends = friends ** 10
    friends **= 12
    print(f"number of friends, after exponent: {friends}")

    friends = friends % 7
    remainder = friends % 7
    print(f"number of friends, after modulos: {friends}")

    print(f"print remaining friends: {remainder}")


    x = 3.14
    y = 4.99
    z = 5.49
    p = -3.2


    result = round(x)
    chop = round(y)
    poop = round(z)
    prop = abs(p) # returns absolute value
    noodle = pow(4, 3) # returns 4^3
    airo = max(x,y,z) # returns value of variable with the highest number
    poodle = min(x,y,z,p) # returns value of variable with the lowest number




    print(result)
    print(chop)
    print(noodle)
    print(poop)
    print(airo)
    print(poodle)