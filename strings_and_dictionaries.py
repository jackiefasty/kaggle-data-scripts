# Strings
x = 'Pluto is a planet'
y = "Pluto is a planet"

print(x==y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

# 'Pluto's a planet!'
# This will give SyntaxError: invalid syntax

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello

print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

# Strings and sequences

# Indexing
planet = 'Pluto'
print(planet[0])

# Slicing
print(planet[-3:])

# How long is this string?
print(len(planet))

# Yes, we can even loop over them
print([char+'! ' for char in planet])

# String methods

claim = "Pluto is a planet"
print(claim.upper())

# All lowercase
claim.lower()

# Searching for the first index of a substring
claim.index('plan')

claim.startswith(planet)

# False because of missing exclamation mark
claim.endswith('planet')

# Split something other than whitespace
datestr = '1956-01-31'
year, month, day = datestr.split('-')

# Dictionaries
# Dictionaries are a built-in Python data structure for mapping keys to values.
numbers = {'one':1, 'two':2, 'three':3}

print(numbers['one'])

numbers['eleven'] = 11
print(numbers)

# To change the value associated with an existing key
numbers['one'] = 'Pluto'
print(numbers)

# Python has dictionary comprehensions with a syntax similar 
# to the list comprehensions we saw in the previous tutorial.
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print('Saturn' in planet_to_initial)

print('Betelgeuse' in planet_to_initial)

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

print(' '.join(sorted(planet_to_initial.values())))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))


