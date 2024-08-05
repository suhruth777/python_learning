# return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function's return value

def multiply(num1, num2):
    result = num1 * num2 # You could remove this line do something like the example on line 17 so you use less code for the same result
    return result

print(multiply(7,7))

#or....

x = multiply(7,7)
print(x)



def multiply_op2(num1, num2): # See comment on line 5
    return num1 * num2

y = multiply(7,7)
print(y)