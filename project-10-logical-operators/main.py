# Run the script by opening the terminal: $ python3 main.py

# Logical Operators (AND / OR / NOT)
# Check for multiple conditions in the same line of code

print('''
I can create multiple lines
of a string
''')

# Use the lower() function to set the value to be lowercase
name = input("What is your name? ").lower()
print(name)
# Use the count() function to count how many times "d" is found in the name
count_letters = name.count("d")
print(count_letters)

# a = 12
# a > 10 and a < 13 (TRUE)

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
    elif age >= 45 and age <= 55:
        print("Have a free ride on us.")
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