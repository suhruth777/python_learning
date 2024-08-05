# scope = The region that a varibale is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name = 'Suhruth' # global version of name

def display_name():
    name = 'Chamarthi' # This variable has a local scope (because it is declared inside of a function)
    print(name)

display_name() # uses local version of name
print(name) # uses global version of name


# If name is not defined inside of function, it will default to the global variable.

