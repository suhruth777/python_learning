# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

name = input("What is your name?: ")
age = int(input("How old are you?: "))
print_again = int(input("How many times do you want to see this message?: "))

year = 2024 - age + 100

for i in range(print_again):
    print(name + " will be 100 years old in " + str(year))


#or....

while print_again > 0:
    print(name + " will be 100 years old in " + str(year))
    print_again += 1
