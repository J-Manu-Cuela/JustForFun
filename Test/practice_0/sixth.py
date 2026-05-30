# Practice 5: Error handling in Python
# This file teaches try/except/finally, raising errors, and custom exception classes.

# A custom exception class inherits from Exception.
class ValidationError(Exception):
    pass


def divide_numbers(a, b):
    # If the divisor is zero, Python cannot divide.
    # We raise a custom exception so the caller can handle it.
    if b == 0:
        raise ValidationError("Cannot divide by zero")
    return a / b

try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except ValidationError as error:
    # This block runs when the custom ValidationError is raised.
    print("Validation error:", error)
except Exception as error:
    # This block catches any other unexpected exception.
    print("Unexpected error:", error)
else:
    # This block runs only if no exception occurred.
    print("Division succeeded")
finally:
    # This block always runs, even if there was an error.
    print("Cleaning up after divide_numbers call")

# A second example showing safe input handling.
text = "abc"
try:
    number = int(text)
    print("Converting to int succeeded:", number)
except ValueError:
    print("ValueError: the text is not a valid integer")
finally:
    print("Finished trying to convert text to int")
