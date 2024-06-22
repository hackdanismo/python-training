# Run the script by opening the terminal: $ python3 main.py

# Conditional Statements (If/Else statements)

# if condition:
#   do this
# else:
#   do this

# Water level example
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

# Equal signs e.g. if height == 120:
# One (=) - value is being assigned, usually to a variable
# Two (==) - checking the value on the left is equal to the value on the right
# Not equals (!=)
# Greater than or equals to (>=) e.g. if height >= 120:
# Less than or equals to (<=) e.g. if height <= 120:

# Ticket example
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("You cannot ride the rollercoaster")

# Nested if/else statement

# if condition:
#   do this
#   if another_condition:
#       do this
#   else:
#       do this
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay £7.")
    else:
        print("Please pay £12.")
else:
    print("You cannot ride the rollercoaster")

# We can use the elif statement to add more conditions to our code

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay £5.")
    elif age <= 18:
        print("Please pay £7.")
    else:
        print("Please pay £12.")
else:
    print("You cannot ride the rollercoaster")

# Modulo (%) gives us the remainder after a division e.g. 6 % 2 = 0 (6 divided by 2 is 3 with no remainder)
# 5 divided by 2 leaves a remainder of 1, so 5 % 2 = 1
number = int(input("Enter a number: "))

# If the number can be divided by 2 with 0 remainder
if number % 2 == 0:
    print("This is an even number.")
# Otherwise, number cannot be divided by 2 with 0 remainder
else:
    print("This is an odd number.")

# Updated BMI Calculator
height = float(input("What is your height? "))
weight = int(input("What is your weight? "))
bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Leap Year
year = int(input("Enter a year: "))
# Can the year be divided by four with no remainder using modulo (%)
if year % 4 == 0:
    # Can the year also be divided by 100 without a remainder
    if year % 100 == 0:
        # Not a leap year, unless special case
        if year % 400 == 0:
            print("Is a leap year.")
        else:
            print("Is not a leap year.")
    else:
        print("Is a leap year.")
else:
    print("Not a leap year.")

# Multiple If statements in succession

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are £5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are £7.")
        bill = 7
    else:
        print("Adult tickets are £12.")
        bill = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add £3 to the bill
        # bill = bill + 3  
        bill += 3           # Is the same as bill = bill + 3  
    print(f"Your final bill is £{bill}.")    
else:
    print("You cannot ride the rollercoaster")