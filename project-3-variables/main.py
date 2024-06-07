# Run the script by opening the terminal: $ python3 main.py

# Variables allow data to be stored in our program

# When naming variables
name = "Dan"
# Separate words with underscores
user_name = "Dan"

# Assigns the value entered into the input() prompt to a variable called name
# For example, name = "Dan"
# Using the print() function to output the value stored in the variable
name = input("What is your name?")
print(name)

# Simplified version to show a simple name being stored
name = "Jack"
print(name)     # Jack
# If we give the variable a new value, the original value will be replaced
name = "Dan"
print(name)     # Dan

# Using variables to return the length of a name
name = input("What is your name?")
length = len(name)
print(length)

# Switching input values
# There are two variables, a and b
a = input("Assembly")
b = input("Basic")
# Create a third variable to help switch the values
# The variable c is a temporary store equal to the variable of a
c = a       # Assembly
# Assign the value of b to the variable of a
a = b       # Basic
# Take to temporary variable and assign its value to b
b = c       # Assembly

print("a: " + a)
print("b: " + b)
