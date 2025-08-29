import math

def run():
    radius = float(input("What is the radius of your circle: "))
    # Area = (radius ** 2) * math.pi 
    # or
    Area = math.pi * pow(radius, 2)
    print(f"The Area of your circle is: {round(Area, 2)}")

    ######## Triangle Hypotenuse ########

    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = math.sqrt(pow(a,2) + pow(b, 2))

    print(f"The hypotenuse of your triangle is: {round(c, 2)}cm")