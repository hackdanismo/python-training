# Run the script by opening the terminal: $ python3 main.py
# Thonny is a useful Python debugging tool

# Comments in Python are written using a hashtag/pound symbol (#)
# Comments can be set using: cmd + / (macOS)

# Using the input() function in Python: input(prompt)
# Used to enter data into our Python code
input("What is your name?")

# The value entered in the prompt will be put back into our code
# This code example will prompt "What is your name?" before returning "Hello Dan" (if Dan is entered in the prompt)
# The input("What is your name?") part of the code is replaced by the name entered e.g. Dan and concatenated to the word "Hello"
# When the prompt is submitted: print("Hello " + "Dan") output: Hello Dan
print("Hello " + input("What is your name?"))

# Using the len() function to get the length of a string
numOfLetters = len("Daniel")
print(numOfLetters)

# Combination that allows users to enter a name and return the length
print(len(input("What is your name?")))