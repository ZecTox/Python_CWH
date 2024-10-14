# Here we are going to see all types of TYPE CONVERSIONS

# 1. Implicit Type Conversion (Coercion)
# This happens automatically by Python when it can safely convert one data type to another without any loss of information. For example:

# Converting an int to a float.

a = 5       # int
b = 2.0     # float
c = a + b   # implicit conversion to float

# 2. Explicit Type Conversion (Type Casting)
# This is done manually using built-in functions. Here are the most common functions used for type conversion:

# int(): Converts a value to an integer.
x = int(3.6)  # x becomes 3

# float(): Converts a value to a float.
y = float(4)  # y becomes 4.0

# str(): Converts a value to a string.
z = str(10)   # z becomes '10'

# list(): Converts a value to a list.
a = list((1, 2, 3))  # a becomes [1, 2, 3]

# tuple(): Converts a value to a tuple.
b = tuple([1, 2, 3])  # b becomes (1, 2, 3)

# set(): Converts a value to a set.
c = set([1, 2, 2, 3])  # c becomes {1, 2, 3}

# dict(): Converts a value to a dictionary, typically from a sequence of key-value pairs.
d = dict([(1, 'one'), (2, 'two')])  # d becomes {1: 'one', 2: 'two'}


#Special Conversions
# bool(): Converts a value to a boolean (True or False)
e = bool(0)  # e becomes False

# Notes on Conversion
# String to Numeric Types: Use int() or float() to convert strings representing numbers.
num = int("123")  # Converts string to int
decimal = float("123.45")  # Converts string to float

# Numeric Types to Strings: Convert using str().

# Complex Numbers: Use complex(real, imag) to create complex numbers.
c_num = complex(1, 2)  # c_num becomes (1+2j)