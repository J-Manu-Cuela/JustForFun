# Practice 2: Functions in Python
# This file explains how to define and call functions.
# It includes positional arguments, default values, *args, **kwargs and return values.

# A simple function with positional arguments:
def multiply(a, b):
    # The function receives two values and returns their product.
    result = a * b
    return result

print("multiply(3, 5)", multiply(3, 5))

# Default argument values:
def greet(name, greeting="Hello"):
    # If the caller does not provide greeting, it uses "Hello".
    return f"{greeting}, {name}!"

print(greet("Manu"))
print(greet("Manu", greeting="Bienvenido"))

# *args collects extra positional arguments as a tuple:
def sum_numbers(first, *args):
    total = first
    for number in args:
        total += number
    return total

print("sum_numbers(2, 3, 4)", sum_numbers(2, 3, 4))

# **kwargs collects extra keyword arguments as a dictionary:
def build_profile(first_name, last_name, **kwargs):
    profile = {
        "first_name": first_name,
        "last_name": last_name,
    }
    # Add any extra fields passed by the caller.
    for key, value in kwargs.items():
        profile[key] = value
    return profile

profile = build_profile("Manu", "Perez", age=30, city="Buenos Aires")
print("Profile:", profile)

# A function can return multiple values as a tuple:
def calculate_area_and_perimeter(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

area, perimeter = calculate_area_and_perimeter(4, 5)
print("Area:", area, "Perimeter:", perimeter)
