# Create a Python program that:

# Asks the user for their age.
# Uses if statements to categorize the user as a child (0-12), teenager (13-19), adult (20-64), or senior (65+).
# Uses logical operators to ensure the age is a valid number (greater than or equal to 0).
# Prints the appropriate category.

age = int(input("Enter you age: "))

if age >= 0 and age <= 12:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 64:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")
else:
    print("Please enter a valid age")
