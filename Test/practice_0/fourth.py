# Practice 3: Comprehensions, generators, and iterators
# This file shows how to build data with list/dict comprehensions and how to use generators.

# List comprehension example:
numbers = [1, 2, 3, 4, 5]
# This creates a new list with each number squared.
squares = [number ** 2 for number in numbers]
print("squares:", squares)

# Dictionary comprehension example:
# Use a comprehension to build key/value pairs.
double_values = {number: number * 2 for number in numbers}
print("double_values:", double_values)

# Generator function example:
# A generator produces values one by one using yield.
def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

# The generator does not produce all values at once.
counter = count_up_to(5)
print("counter is an iterator", counter)
print("first value:", next(counter))
print("second value:", next(counter))

# You can iterate over the generator with a for loop:
for value in count_up_to(3):
    print("generated value:", value)

# Using iterators manually:
text = "Python"
text_iterator = iter(text)
print("First character:", next(text_iterator))
print("Second character:", next(text_iterator))

# If there are no more values, next() raises StopIteration.
try:
    while True:
        char = next(text_iterator)
        print("More char:", char)
except StopIteration:
    print("No more characters in the iterator.")
