# Loops and List Comprehensions

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # Print all on same line


multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
    print(product)
print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')  

# Range function
for i in range(5):
    print("Doing important work for this Kaggel certificate. i =", i)

# While loops
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # Increase the value of i by 1

# List comprehensions
squares = [n**2 for n in range(10)]
print(squares)

squares = []
for n in range(10):
    squares.append(n**2)
print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

# We can also split it in 3 lines, maybe more convenient? 
[
    print(planet.upper() + '!') 
    for planet in planets 
    if len(planet) < 6
]
# But then the results are line by line

[32 for planet in planets]

def count_negatives_v1(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

print(count_negatives_v1([5, -1, -2, 0, 3]))

def count_negatives_v2(nums):
    return len([num for num in nums if nums < 0])

# print(count_negatives_v2([5, -1, -2, 0, 3])) 
# Why not working? 
# TypeError: '<' not supported between instances of 'list' and 'int'

def count_negatives_v3(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])

print(count_negatives_v3([5, -1, -2, 0, 3]))

