# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of positional arguments

def add(num1, num2):
    sum = num1 + num2
    return sum

# print(add(1,2,3)) # This doesn't work because there are 3 arguments and function only has 2 parameters

# Use args to circumvent this issue

def new_add(*args): # the * is important, args is not. You can name it whatever you want
    sum = 0
    for i in args: # args is always a tuple
        sum += i
    return sum

print(new_add(1,2,3))
print(new_add(1,2,3,5,6,3,1)) # Can add as many arguments as you'd like


def change_add(*stuff): 
    sum = 0
    stuff = list(stuff) # changes tuple to list so we can change it
    stuff[0] = 0 # makes it so that the first argument in function call (line 30) is changed to 0
    for i in stuff: 
        sum += i
    return sum

print(change_add(1,2,3,5,6,3,1)) # See that the result is 20 insated of 21, since 1 is changed to 0