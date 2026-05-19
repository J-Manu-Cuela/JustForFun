# Summary of Python Data Types with Examples

# 1. Numeric Types
# int: Represents integers (whole numbers)
x = 10  # Example of an integer
# Interesting: Python integers can grow arbitrarily large, limited only by memory.

# float: Represents floating-point numbers (decimal numbers)
y = 3.14  # Example of a float
# Interesting: Floats are implemented using double in C, so they have precision limits.

# complex: Represents complex numbers with real and imaginary parts
z = 2 + 3j  # Example of a complex number
# Interesting: Useful in scientific computing and signal processing.

# 2. Sequence Types
# str: Represents strings (text data)
name = "Python"  # Example of a string
# Interesting: Strings are immutable, meaning they cannot be changed after creation.

# list: Represents ordered, mutable collections
fruits = ["apple", "banana", "cherry"]  # Example of a list
# Interesting: Lists can hold mixed data types.

# tuple: Represents ordered, immutable collections
coordinates = (10, 20)  # Example of a tuple
# Interesting: Tuples are faster than lists due to immutability.

# 3. Mapping Type
# dict: Represents key-value pairs
person = {"name": "Alice", "age": 25}  # Example of a dictionary
# Interesting: Dictionaries are implemented as hash tables, making lookups very fast.

# 4. Set Types
# set: Represents unordered collections of unique elements
unique_numbers = {1, 2, 3}  # Example of a set
# Interesting: Sets are useful for removing duplicates.

# frozenset: Immutable version of a set
frozen = frozenset([1, 2, 3])  # Example of a frozenset

# 5. Boolean Type
# bool: Represents True or False
is_active = True  # Example of a boolean
# Interesting: Booleans are a subclass of integers (True is 1, False is 0).

# 6. Binary Types
# bytes: Represents immutable sequences of bytes
data = b"hello"  # Example of bytes

# bytearray: Mutable version of bytes
data_mutable = bytearray(b"hello")  # Example of bytearray

# memoryview: Provides a view of the memory of another binary object
view = memoryview(b"hello")  # Example of memoryview

# 7. None Type
# NoneType: Represents the absence of a value
value = None  # Example of NoneType
# Interesting: Commonly used as a default value for optional parameters.

# 8. Specialized Types
# range: Represents an immutable sequence of numbers
r = range(5)  # Example of range (0, 1, 2, 3, 4)

# enumerate: Adds a counter to an iterable
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)