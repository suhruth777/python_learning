# list = used to store multiple items in a single variable

food = ['pizza', 'burger', 'hotdog', 'pasta', 'pudding']

print(food) # prints whole list
print(food[1]) # prints value held by index number
print(food[::-1]) # prints list in reverse

food[0] = 'sushi' # changes pizza to sushi

for i in food: # prints each item individually
    print(i)

# List Manipulation

food.append("ice cream") # adds specified item to list
food.remove("hotdog") # removes specified item to list
food.pop() # removes last item in list
food.insert(0, "cake") # adds item in chosen index position
food.sort() # organizes list into alphabetical order
food.clear() # removes all elements in list
