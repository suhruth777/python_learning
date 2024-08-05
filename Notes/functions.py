# function = a block of code which is executed only when it is called

def hello(name): # name is a parameter that goes in the parentheses of the function
    print('Hello ' + name)
    print("Have a nice day!")

hello("Suhruth") # Runs the function above
                 # Sends argument ("Suhruth") and assigns it to the parameter held in the function defintion which is "name"

my_name = "Suhruth"
hello("Bob") # Can assign anything as an argument for the parameter
hello(my_name) # Define varibale and then call it in the function so it is then an arugment that is given to the parameter in the function

# hello("Bro", "Code") # This doesn't work because you have given two arguments to the functions that only has one parameter

def new_hello(first_name, last_name, age): # Has three parameters
    print("Hello", first_name, last_name)
    print('You are', str(age), "years old") # Convert int to str for string combining
    print("Have a nice day!")

new_hello('Suhruth', 'Chamarthi', 21) # Gives three arguments