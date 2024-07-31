# Create a Python program that acts as a simple calculator. The program should:
# Ask the user for two numbers.
# Ask the user for the type of operation they want to perform (addition, subtraction, multiplication, or division).
# Perform the operation and print the result.
# Use type casting, if statements, and user input.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operation = input("Choose to +, -, *, or / your two numebrs: ")

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print('Please enter a valid operation.')
