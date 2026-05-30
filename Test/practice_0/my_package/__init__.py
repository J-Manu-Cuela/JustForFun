# my_package is a simple Python package.
# This __init__.py file makes Python treat this folder as a package.

from .operations import multiply, greet_person

__all__ = ["multiply", "greet_person"]
