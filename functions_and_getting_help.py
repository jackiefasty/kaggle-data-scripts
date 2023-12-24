import pandas as pd
import numpy as np

#help(round)
#help(round(-2.01))
#help(print)

# Defining functions
def least_difference(a, b, c):
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)

    return min(diff1, diff2, diff3)

answer = least_difference(9, 3, 5)
print(answer)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), 
    # Python allows trailing commas in argument lists. How nice is that?
)

#help(least_difference)

def least_difference_with_docstring(a, b, c):
    """Return the smallest difference between
    any two numbers among a, b and c.
    
    >>> least_difference()"""

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    
    return min(diff1, diff2, diff3)

#help(least_difference)

def least_difference_no_return(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

mystery = print()
print(mystery)

print(1, 2, 3, sep=' < ')

def greet(who="Jaume"):
    print("Hello, ", who)

greet()
greet(who="Borja")
greet("World")

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    "Call fn on the result of calling fn on arg"
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)