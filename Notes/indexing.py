# index operator [] = gives access to a sequence's element (str, list, tuples)

name = 'suhruth Chamarthi!'

# if(name[0].islower()): # will be True or False
#     name = name.capitalize()

first_name = name[:7].upper() # Returns first name and capitalizes it
last_name = name[8:].lower() # Returns last name and makes it lowercase
last_character = name[-1] # Returns last element in sequence

print(first_name)
print(last_name)
print(last_character)