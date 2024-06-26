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

# Functions with Inputs
# Caeser Cipher - ancient encryption

# This function has a parameter to allow data to be passed into the function
def my_function(something):
    print(something)

# We call the function and pass a value into the function using an argument
my_function(123)

# def my_function(parameter):
#   # Do something here
#
# my_function(argument)

# Functions with more than one input
# Positional Arguments - where the arguments have to be in the correct order to match with the order of the parameters
def greet_with(name, location):
    # Using f-String to output the value entered into the function
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Dan", "Sussex")

# Keyword Arguments - adding each of the parameter names to the arguments so order doesn't matter
def greet_with_location(name, location):
    # Using f-String to output the value entered into the function
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_location(location="Sussex", name="Dan")

# The return statement tells to computer that this is the end of the function execution and exit the function

# Functions with Output
def my_calc_function():
    result = 3 * 2
    # The keyword of return is the output keyword - whatever I want to output when I call the function
    return result

output = my_calc_function()
print(output)

# Convert a String to Title case in Python
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()  # Convert to Title case
    formatted_l_name = l_name.title()  # Convert to Title case

    #print(f"{formatted_f_name} {formatted_l_name")
    return f"{formatted_f_name} {formatted_l_name}"

#formatted_string = format_name("dAn", "sMIth")
#print(formatted_string)

print(format_name("dAn", "sMIth"))

# Multiple Return Values

# Convert a String to Title case in Python
def format_name_update(f_name, l_name):
    # Check to see strings are not empty
    if f_name == "" or l_name == "":
        # Else/Terminate the function if the strings are empty to exit the function
        return "You didn't provide valid inputs."
    else:
        formatted_f_name = f_name.title()  # Convert to Title case
        formatted_l_name = l_name.title()  # Convert to Title case
        return f"{formatted_f_name} {formatted_l_name}"


print(format_name_update(input("What is your first name? "), input("What is your last name? ")))

# Multi-line comments
# Highlight the code or comment
# Mac: cmd + /
# Windows: ctrl + /

# This is a multiline comment
# added to my Python code
# to demonstrate this

# Docstrings - automated documentation for our functions and code blocks
# Docstrings - """ """

# Convert a String to Title case in Python
def format_name_update_docstrings(f_name, l_name):
    # This is a Docstring for automated documentation - can be over multiple lines
    """Take a first and last name and format it 
    to return the title case version of the name."""
    # Check to see strings are not empty
    if f_name == "" or l_name == "":
        # Else/Terminate the function if the strings are empty to exit the function
        return "You didn't provide valid inputs."
    else:
        formatted_f_name = f_name.title()  # Convert to Title case
        formatted_l_name = l_name.title()  # Convert to Title case
        return f"{formatted_f_name} {formatted_l_name}"


print(format_name_update_docstrings(input("What is your first name? "), input("What is your last name? ")))
