# note: you may want to run python without
# buffering. You do this bay calling the
# module with teh command python -u dec04.py
# try it both buffered and unbuffed to see
# difference
from time import sleep
import sys

def slow_your_roll(function):
    def wrapper(*args, **kwargs):
        print("About to call function:", function.__name__)
        sleep(1)
        function(*args, **kwargs)
    return wrapper

@slow_your_roll
def some_function(x):
    print("# -> "+str(x))

@slow_your_roll
def some_other_function(x,y):
    print("# -> "+str(x) + " -- ", str(y))

for i in range(3):
    some_function(i)

for i in range(3):
    some_other_function(i, i*2)
