# dictionary = A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC', 
            'India':'New Dehli', 
            'China':'Beijing', 
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # adds key:value pair
capitals.update({'USA':'Princeton'}) # updates key:value pair
capitals.pop('China') # removes pair
capitals.clear() # clears dictionary

print(capitals['Russia']) # If you put a key in this that doesn't exist, it will stop your code
print(capitals.get('Germany')) # Safe way of checking if there is a key within your dict

print(capitals.keys()) # prints just the keys
print(capitals.values()) # prints just the values
print(capitals.items()) # prints entire dictionary

for key, value in capitals.items(): # Loop to print entire dictionary
    print(key, value)