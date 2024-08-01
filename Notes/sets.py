# set = collection which is unordered, unindexed. Does not allow duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}


utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes) # put dishes into utensils
dinner_table = utensils.union(dishes) # joins dishes and utensils into a new set

print(utensils.difference(dishes)) # shows what utensils has that dishes doesn't
print(utensils.intersection(dishes)) # shows what utensils and dishes have in common



for i in dinner_table:
    print(i)

