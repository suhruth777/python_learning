# Problem: Factorial Function
# Write a function factorial(n) that returns the factorial of a given number n. 
# Use recursion to implement this function.

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
print(factorial(0))
print(factorial(1))

# Problem 5: Temperature Conversion
# Write a function celsius_to_fahrenheit(celsius) that takes a temp in C and converts it to F. 
# The formula for the conversion is: F = C * 9/5 + 32

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(celsius_to_fahrenheit(17))