import time
from datetime import date
from random import *

def hello_world():
    print("Hello World!")
    return

def print_date():
    today = date.today()
    print("Today's date: ", today)
    return

def print_random_number():
    random_int = randint(1, 100)
    print("Today's lucky number: %d" % (random_int))
    return 

def print_time(startTime: float, endTime: float):
    print("Finished in %0.4f seconds" % (endTime - startTime))
    return

def main():
    startTime = float(time.time())
    hello_world()
    print_date()
    print_random_number()
    endTime = float(time.time())
    print_time(startTime, endTime)
    return

if __name__ == '__main__':
    main()