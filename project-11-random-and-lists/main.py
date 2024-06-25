# Run the script by opening the terminal: $ python3 main.py

## Randomisation
# Python uses Mersenne Twister algorithm for random number generation
# Python has a built-in module to use random

# Modules
# Allows code to be split up into individual modules
# The main.py is the entry point to our program

# We first have to import this module
import random
# Import my_module.py
import my_module

# Using the randint() method of the random module
# This will return a random whole number between 1 and 10 (inclusive of both values)
random_integer = random.randint(1, 10)
print(random_integer)

# This will return a random floating point number between 0.0 and 1.0
random_float = random.random()
print(random_float)

# This will return a random floating point number between 0 and 5
random_float_updated = random.random() * 5
print(random_float_updated)

# Print the value from the my_module.py module file
print(my_module.pi)

# Coin toss example
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

## Lists
# The list in Python is a Data Structure (organising and storing data)
# A variable is a method to store a single piece of data
# Lists are similar to arrays
# example: fruits = [item1, item2]
# example: fruits = ["Cherry", "Apple", "Pear"]

states_of_america = ["Delaware", "Pennsylvania"]
print(states_of_america)        # Output: ["Delaware", "Pennsylvania"]
print(states_of_america[0])     # Output: Delaware
print(states_of_america[-1])    # Count from the end of the list when using minus values

# Update the second item in the list to "test" from "Pennsylvania"
states_of_america[1] = "test"
print(states_of_america)

# Use the append() method to add a new state to the list as a single item
states_of_america.append("New State")
print(states_of_america)

# Use the extend() method to add a list to the existing list for adding multiple items
states_of_america.extend(["New York", "Florida"])
print(states_of_america) 

# Return the number of items in the list using the len() function
print(len(states_of_america))

# Return the last item in the list without needing the index
number_of_states = len(states_of_america)
print(states_of_america[number_of_states - 1])

# New list
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Nested lists - list within a list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

nested_dirty_dozen = [fruits, vegetables]
# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
print(nested_dirty_dozen)
# Kale - Second list (index of 1), Second item (index of 1)
print(nested_dirty_dozen[1][1])
# Nectarines - First list (index of 0), Second item (index of 1)
print(nested_dirty_dozen[0][1])