# Run the script by opening the terminal: $ python3 main.py

# Create a greeting for the program
print("Welcom to the band name generator.")
# Ask the user for the city that they grew up in and store in variable
# Use \n to move cursor to a new line
city = input("Which city did you grow up in?\n")
# Ask the user for the name of a pet and store in a variable
# Use \n to move cursor to a new line
pet = input("What is the name of a pet?\n")
# Combine the name of their city and pet and show them their band name using String concatenation
print("Your band name could be: " + city + " " + pet)