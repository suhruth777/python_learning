# Create a Python program that:

# Asks the user to guess a number between 1 and 100.
# Uses a while loop to allow the user to keep guessing until they get the correct number.
# Uses if statements to tell the user if their guess is too high, too low, or correct.
# Generates a random number for the user to guess using the random module.

import random

num = int(input('Guess a number between 1 and 10: '))
correct_num = random.randrange(1,10)

while num != correct_num:
    num = int(input('Guess a number between 1 and 10: '))

print("Good job! The correct answer was in fact: " + str(correct_num))

