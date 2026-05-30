# Practice 7: Modules and packages in Python
# This file shows how to import code from another module and from a package.
# The helper files are in the same folder and the my_package package.

# Import an entire module.
import helper_module

# Import specific names from a module.
from helper_module import add_numbers

# Import from a package.
from my_package import multiply, greet_person

print(helper_module.greet("Manu"))
print("add_numbers(4, 7):", add_numbers(4, 7))
print("multiply(3, 5):", multiply(3, 5))
print(greet_person("Manu"))

# A simple function to show module behavior.
def describe_imports():
    # This function uses names imported above.
    print("This file imported helper_module and my_package successfully.")

if __name__ == "__main__":
    describe_imports()
