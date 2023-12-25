# Lists

# List of integers
primes = [2, 3, 5, 7]

# List of strings
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Two lists of lists
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # The comma after the last element is optional)
]

hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

# List with different types of variables
my_favourite_things = [32, 'raindrops on roses', help]

# Indexing

# Let's go towards indexing in lists
print(planets[0])
print(planets[1])
print(planets[2])
print(planets[-1])
print(planets[-2])
# Elements at the end of the list can be accessed with negative numbers, starting from -1

# Slicing

print(planets[0:3]) # Until 3rd element, including it
print(planets[:3]) # Until 3rd element, including it
print(planets[3:]) # Starting from 3rd element (without including it),
# i.e. starting from 4th element including it
print(planets[1:-1]) # All the planets except the first and last
print(planets[-3:]) # The last 3 planets

# Changing lists

planets[3] = 'Malacandra'
print(planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']

# List functions
len(planets)

# Sort strings alphabetically
sorted(planets)

# Sum values from a list
primes = [2, 3, 5, 7]
sum(primes)

# Return biggest number on a list
print(max(primes))

# Interlude objects
x = 12
# x is a real number, with imaginary part of 0
print(x.imag)

# Make a complex number
c = 12 + 3j
print(c.imag)

x.bit_length

# Call the function
x.bit_length()

# List methods

# Append string element to a list
planets.append('Pluto')
print('Planets list status?: ', planets)

print(planets.pop())

# Searching lists

# Search element on a list using 'index'
print(planets.index('Earth'))
print(planets.index('Pluto'))
print("Earth" in planets)
print("Calbefraques" in planets)




