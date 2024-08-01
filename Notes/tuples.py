# tuple = collection which is ordered and unchangeable used to group together related data

student = ("Suhruth", 22, "male",)

print(student.count("Suhruth")) # counts how many times "Suhruth" appeards in tuple
print(student.index("Suhruth")) # gives positioning of "Suhruth" in tuple

for i in student:
    print(i)

if "Suhruth" in student:
    print("Suhruth is here")