# Countdown Timer
import time 


def run():
    my_time = int(input("Enter the time in seconds: "))

    # for i in range(0, my_time):
    for i in range(my_time, -1, -1):
        seconds = i % 60
        minutes = int(i / 60) % 60
        hours = int((i / 60) / 60) # you can add % 24 to calculate 24 hours in a day, but we don't have days included
        print(f"{hours:02}:{minutes:02}:{seconds:02}") # :02 does 0 padding, the 2 signifies to make the value double digit, inserting an empty 0
        
        time.sleep(1) # makes program wait 1 second between each number being printed
    print("TIME'S UP!")
    for i in range(my_time, 0, -1): # this will print up to 1 second, make the second paramater -1
    # for i in range(my_time, -1, -1) # this will print up to 0 seconds
        print(i)
        time.sleep(1)
    print("TIME'S UP!")