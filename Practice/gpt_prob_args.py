# Problem: Sum of Arbitrary Arguments
#   Write a function sum_all_args(*args) that takes any number of arguments and returns their sum.
#   If no arguments are passed, return 0.

def sum_all_arg(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_all_arg()) # returns 0
print(sum_all_arg(2,3,5,1)) # returns 11

# Problem: Maximum of Arbitrary Arguments
#   Write a function max_arg(*args) that takes any number of arguments and returns the maximum value. 
#   If no arguments are passed, return None.

def max_arg(*args):
    if not args:
        return None
    return max(args)

print(max_arg())