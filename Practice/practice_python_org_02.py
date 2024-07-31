# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.
#  Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. 
# If not, print a different appropriate message

even_odd = int(input("Enter a number, I will tell you if it is even or odd: "))

if even_odd % 2 > 0:
    print("The number you entered is odd")
elif even_odd % 4 == 0:
    print("The number you entered is a multiple of 4")
else:
    print("The number you entered is even")

num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

if num % check == 0:
    print(str(num) + " is divisble by " + str(check))
else:
    print(str(num) + ' is not divisble by ' + str(check))



