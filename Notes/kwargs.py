# **kwargs = parameter that will pack all argument into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(first, last):
    print("Hello", first, last)

# hello(first='Suhruth', middle='blah',last='Chamarthi') # This won't work because there are 3 keyword args when func only has 2 parameters

# Below is an exmaple of kwargs usage in order to account for a varying amt of keyword arguments

def hello_v2(**kwargs): # like args, you don't need to call it kwargs. Only the ** are required
    #print("Hello", kwargs['first'], kwargs['second']) # Use kwargs to call the right key and get the right value in the output
    print("Hello", end=" ")
    for key,value in kwargs.items(): # loops through dictionary and prints only the values
        print(value, end=" ")

hello_v2(title="Mr.", first="Suhruth", last="Chamarthi")