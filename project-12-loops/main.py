# Run the script by opening the terminal: $ python3 main.py

# Loops
# This is a for loop

# for item in list_of_items:
#   # Do something to each item

fruits = ["Apple", "Peach", "Pear"]
# Print out each of the items in the list using a for loop
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Input a list of student scores to get the highest score
# Scores can be entered like this: 23 34 76 12 15 16
student_scores = input("Enter scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
# Loop through the list of student scores
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# For loops with the range() function

# for number in range(a, b):
#   print(number)

# This for loop will print every number between 1 and 9, but not 10
for number in range(1, 10):
    print(number)

# We can add a third value to specify the step size (3)
# This will return 1, 4, 7 (3 numbers between each value returned)
for number in range(1, 10, 3):
    print(number)

# Add all numbers between 1 and 100
total = 0
for number in range(1, 101):
    # Use accumulator to add each number in the range together
    total += number
# This should return 5050 (1+2+3 .... +100)
print(total)

# Return all even numbers
target = int(input("Number between 0 and 1000: "))
even_sum = 0
# For loop to loop through the numbers in the range starting with 2 which is the first even number
# range(start number, end number, increment)
# target + 1 is used because the range will stop just before the last value without the + 1
# e.g. number entered is 1000 - range (2, 1000 + 1, 2)
# The final number of 2, is how much we want to add to the number on each loop
for number in range(2, target + 1, 2):
    print(number)

# Get the total of all even numbers
target = int(input("Number between 0 and 1000: "))
even_sum = 0
# For loop to loop through the numbers in the range starting with 2 which is the first even number
# range(start number, end number, increment)
# target + 1 is used because the range will stop just before the last value without the + 1
# e.g. number entered is 1000 - range (2, 1000 + 1, 2)
# The final number of 2, is how much we want to add to the number on each loop
for number in range(2, target + 1, 2):
    # accumulate even_sum here
    even_sum += number
print(even_sum)

# Alternative method
alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)


