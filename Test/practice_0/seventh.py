# Practice 6: Basic Object-Oriented Programming (OOP)
# This file teaches how to create classes, use __init__, self, attributes, methods, and simple inheritance.

class Animal:
    def __init__(self, name, species):
        # __init__ is the constructor. It sets up the object when it is created.
        self.name = name
        self.species = species

    def speak(self):
        # A method is a function that belongs to an object.
        return f"{self.name} the {self.species} makes a sound."


class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class constructor with super().
        super().__init__(name, "dog")
        self.breed = breed

    def speak(self):
        # Override the parent method for dog-specific behavior.
        return f"{self.name} the {self.breed} says: woof!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "cat")
        self.color = color

    def speak(self):
        return f"{self.name} the {self.color} cat says: meow."


my_dog = Dog("Fido", "Labrador")
my_cat = Cat("Mia", "black")
print(my_dog.speak())
print(my_cat.speak())

# Inspect object attributes.
print("Dog name:", my_dog.name)
print("Dog species:", my_dog.species)
print("Cat color:", my_cat.color)
