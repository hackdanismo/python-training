# Run the script by opening the terminal: $ python3 main.py

# If the bill was £150.00, split the bill between 5 people, with a 12% tip.

# Each person should pay (150.00 / 5) + 1.12 = 33.6
# 12% is equal to 12 / 100 = 0.12
# 150 (total bill) * 0.12 (12% of the total bill) = 18.0
# Add the tip to the final bill (150 + 18.0) = 168
# Shorthand is: 150 * 1.12 = 168.00000000000
# 168 / 5 (people) = 33.6
# Format the result to 2 decimal places = 33.60

## Tip Calculator
print("Welcome to the tip calculator.")
# Collect the bill amount as a string and convert it to a float
bill = float(input("What was the total bill? £"))
# Collect the tip amount as a string and convert it to an integer
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# Collet the number of people as a string and convert it to an integer
people = int((input("How many people to split the bill? ")))

# Calculate the tip
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
# final_amount = round(bill_per_person, 2)  # Using round() may lead to 33.6 (without the 0 on the end)
# Turn float into a string
final_amount = "{:.2f}".format(bill_per_person)     # Using format() to ensure we fix this to always be 2 decimal places but be 33.60

print(f"Each person should pay: £{final_amount}")