# keyword arguments = arguments preceeded by an identifier when we pass them to a function.
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arugments that our function recieves

# Below is an example of positional arugments
def hello(first, last):
    print("Hello", first, last)

hello('Suhruth', 'Chamarthi') # Order of the arguments matters here, if you switched S and C, it would show it backwards and wrong

# Below is the same function call but this time with keyword arguments
hello(last = "Chamarthi", first = "Suhruth") # Prints in correct order because we used keyword arguments