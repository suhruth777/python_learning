# nested function calls = function calls indside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

num = input("Enter a whole positive number: ") # The code below makes sure the end result is a whole positive number
num = float(num)
num = abs(num)
num = round(num)
print(num)

#Or.....

print(round(abs(float(input("Enter a whole positive number: "))))) # Does the same thing as the code above with less lines