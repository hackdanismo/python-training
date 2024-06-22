# Run the script by opening the terminal: $ python3 main.py

# Mathematical operations/operators
# 3 + 5 (addition)
# 7 - 4 (subtraction)
# 3 * 2 (multiplication)
# 6 / 3 (division) - always ends with a floating (float) point number e.g. 2.0
# ** (exponent) - e.g 2 ** 2 (2 to the power of 2)

print(type(6 / 3))      # <class 'float'>
print(2 ** 2)           # 2 to the power of 2 (2 x 2) = 4
print(2 ** 3)           # 2 x 2 x 2 = 8

print(3 * 3 + 3 / 3 - 3)    # 7.0
# Thonny as a tool can be used to debug and walk through this code calculation
# Using the PEMDAS rule: () then ** then * / then + -
print(3 * (3 + 3) / 3 - 3)  # 3.0 - brackets calculated first (3 + 3 becomes highest priority calculated first)

## BMI Calculator
height = input("What is your height?")
weight = input("What is your weight?")
# Convert the weight to be an integer as kg (e.g 69)
weight_as_int = int(weight)
# Convert the height to be an float in meters (e.g. 1.63)
height_as_float = float(height)
# Calculate the BMI (Weight / Height * Height) using the exponent operator (**) to square the height
bmi = weight_as_int / height_as_float ** 2
# OR, using multiplication and PEMDAS/BODMAS
# bmi = weight_as_int / (height_as_float * height_as_float)
# Convert the BMI to be an int so it becomes a whole number
bmi_as_int = int(bmi)
print(bmi_as_int)

# Rounding numbers
print(8 / 3)                # 2.6666666666666665
# Use the round() function to round a float to be a whole number
print(round(8 / 3))         # 3
# Round the number to 2 decimal places
print(round(8 / 3, 2))      # 2.67
# Normal division (single /) returns a floating point number
# Floor division (two //) this returns an integer rather than a float
print(8 // 3)               # 2

result = 4 / 2              # 2 stored in a variable
result /= 2                 # The value of result (2) divide by 2
print(result)               # 1.0

# Increment value
score = 0
score += 1                  # Increment score by 1
print(score)

# Decrement value
score = 0
score -= 1                  # Decrement score by 1
print(score)

# Multiply & Divide
score *= 1
score /= 1

# f-Strings in Python
score = 0
# This will return a type error as this is a string and integer
# print("Your score is " + score)
# Instead, convert the integer into a string
# print("Your score is " + str(score))

# To avoid having to use "+" and to convert data types to output, we can use f-String
score = 0
height = 1.6
isWinning = True
# f-String (add an "f" in-front of the string) - allows converting to be done behind the scenes
print(f"Your score is {score}, your height is {height}, we are winning {isWinning}")

## Weeks left
age = input("How old are you?")
# Maximum expected lifespace of 90 years minus the age entered converted to an integer
years = 90 - int(age)
# Calculate the number of weeks of the remaining years (52 weeks per year)
weeks = years * 52

print(f"You have {weeks} weeks left.")