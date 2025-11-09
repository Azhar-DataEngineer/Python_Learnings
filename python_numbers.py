x = 5   
y = 5.7
z = 2 + 3j

# Checking the types of the numbers
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>       
print(type(z))  # Output: <class 'complex'>

x = "2"

print(type(x))  # Output: <class 'str'>
print(x * 3)
# 5.50

x = int(x)

print(type(x))

print(x * 3)

x = 3.14

print(int(x))

x = 3

print(float(x))

x = 3
y = 2
print(complex(x, y))
print(complex(x))  # Imaginary part will be 0 by default


x = 3

# Shorthand assignment operators
x += 2  # Equivalent to x = x + 2
print(x)  # Output: 5

# Rounding a number - function 

# measure distance

print(abs(2-8))  # Output: 6

# Rounding numbers

price = 35.7428373827403  
print(round(price, 2))  # Rounds to 2 decimal places

price = 35.5487938427403

print(round(price))

import math 

print(math.floor(price))  # Requires import from math module

print(math.ceil(price))  # Requires import from math module

print(math.trunc(price))  # Requires import from math module

import random

print(random.random())

print(random.randint(1, 2))  # Random integer between 1 and 100 inclusive

x = 7.0 

x.is_integer()  # Returns True if the float is an integer value
print(x.is_integer())

y = 7.5
print(y.is_integer())  # Output: False

x = 70.9

isinstance(x, int)  # Returns True if x is an integer
print(isinstance(x, int))


num = random.randint(1, 100)  # Random integer between 1 and 100 inclusive

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")