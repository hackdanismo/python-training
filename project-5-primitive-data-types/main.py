# Run the script by opening the terminal: $ python3 main.py

# Data Types:
# String - "Hello"
# Integer (whole numbers) - 12345
# Large Integer - 342,654,896
# Float - (numbers with decimal places - floating point number) - 1.2 
# Boolean - True/False

# Using the len() function to get the number of characters (5) in a string
print(len("Hello"))
# This will return an error if we use numbers as object of type "int" has no len()
# print(len(12345))

# This next approach of pulling out a character from a String is called: Subscript
# This will return the first character (H) in the String as index is set to 0
print("Hello"[0])
# This will return the first character (E) in the String as index is set to 1
print("Hello"[1])

# Integers - will calculate the total and print the output (468)
print(123 + 345)
# Large integers (342,654,896) would be 342_654_896 in Python (replace comma with underscore) for readability

# We cannot concatenate (join) strings and integers together initially

# Return the data type of the value using the type() function
# This is used for type checking
print(type("Hello"))    # <class 'str'>
print(type(12345))      # <class 'int'>

# Type conversion (type casting) - change data from one data type to another
# Convert integer to a string using str() function
str(12345)

num_char = len(input("What is your name?"))
# Convert the input value from an integer (length of the name), to a string using str() and store in a variable
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Convert a number to a string
a = 12345
print(type(a))     # This will return <class 'int'>

a = str(12345)
print(type(a))      # This will return <class 'str'> as converted to string using str() function

a = float(12345)
print(type(a))      # Converts to a float using the float() function

# Convert the string of "100.5" to a float (100.5) then add 70 = 170.5
print(70 + float("100.5")) 