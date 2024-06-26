# Run the script by opening the terminal: $ python3 main.py

# Indentation
# Cannot mix tabs and spaces for indentation in a Python 3 file.
# Use 4 spaces per indentation level
# Python Style Guide: https://peps.python.org/pep-0008/

# Functions
# Name of the function followed by a set of parenthesis ()
# Python built-in functions: https://docs.python.org/3/library/functions.html
print("This is using the built-in print() function in Python.")
# Using the len() function to see how many characters are in the word "Hello"
print(len("Hello"))

# Defining (creating) our own functions uses the keyword of "def"
def my_function():
    # This is the code block of the function where we execute the code
    print("Hello")
    print("Bye")

# Calling the function to execute the codein the function
my_function()

# While Loop

# while something_is_true:
#   Do something repeatedly

# Infinite loop - the code will continually run without an end
# If value of 5 is greater than 3 (always true)
# while 5 > 3:
#   # Do this - forever as an infinate loop (not ideal)