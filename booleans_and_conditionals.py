# Booleans
x = True
print(x)
print(type(x))

# Comparison Operations
def can_run_for_president(age):
    """Can someone of the given age run for preisent of the US?
    >>> can_run_for_president(27)
    False
    """
    # US Constitution says you must be at least 35 years old
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))

print(3.0 == 3)
print(3.1 == 3)

print('3' == 3)

def is_odd(n):
    """Tells if the input number is odd or not.
    >>> is_odd(7)
    True
    """
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

# Combining Boolean values
def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(27, False))

print(True or False and False)

# Conditionals
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is kind of weird? What's that mate")

inspect(6)
inspect(0)
inspect(-50)

def f(x):
    if x > 0:
        print("Only printed when x is positive; x =", x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)

# Boolean conversion
print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))

# We can use non-boolean objects in if conditions and other places where a boolean would be expected. 
# Python will implicitly treat them as their corresponding boolean value:

if 0:
    print(0)
elif "spam":
    print("spam")