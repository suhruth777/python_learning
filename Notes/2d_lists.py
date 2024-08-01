# 2D Lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "burger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert] 

print(food) # prints a list of the lists inside of the food variable

print(food[0]) # will give you list in position 0
print(food[0][1]) # will return item in position 1 in list in position 0: soda

