# Practice 1: Control flow in Python
# This file covers the main ways Python decides what code to run.
# It includes conditionals, loops, and special loop controls.

# Example of if / elif / else:
# Python checks the conditions in order. The first one that is True runs.
number = 7
if number < 0:
    print("number is negative")
elif number == 0:
    print("number is zero")
else:
    print("number is positive")

# for loop over a list:
# "for" repeats an action for each item in a sequence.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    # This line runs once for every fruit in the list.
    print("Fruit:", fruit)

# while loop with break and continue:
# "while" repeats as long as a condition stays True.
count = 0
while count < 5:
    count += 1
    if count == 3:
        # "continue" skips the rest of this loop iteration.
        print("Skipping number 3")
        continue
    if count == 5:
        # "break" stops the loop completely.
        print("Reached 5, stopping")
        break
    print("Current count:", count)

# match / case (Python 3.10+):
# It is similar to switch/case in other languages.
value = "open"
match value:
    case "open":
        print("The door is open")
    case "closed":
        print("The door is closed")
    case _:
        # The underscore means "anything else".
        print("Unknown door state")
