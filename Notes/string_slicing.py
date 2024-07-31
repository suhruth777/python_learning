#slicing: create a substring by extracting elements from another string
#   You can indexing[] or slice()
#   [start:stop:step]

#index function
name = 'Suhruth Chamarthi'

first_name = name[0:7] #prints Suhruth
first_name = name[:7] #same as line 7 (shorthand)
print(first_name)

last_name = name[8:17] #prints Chamarthi
last_name = name[8:] #same as line 11 (shorthand)
print(last_name)

funky_name = name[0:17:3] #grabs every third character
funky_name = name[::3] #same as line 15 (shorthand)
print(funky_name)

reversed_name = name[::-1] #reverses string
print(reversed_name) 

#slice function
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) #cuts 7 from the left, cuts 4 from the right. Isolates google
print(website1[slice]) #put slice variable into index
print(website2[slice])

