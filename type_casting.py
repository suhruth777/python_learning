#Type Casting: convert the data type of a value to another data type

x = 1 #int
y = 2.0 #float
z = "3" #string

x = float(x) #Changes int to float
y = int(y) #Changes float into int
z = float(z) #Changes str to float

print(x)
print(y) #prints int rather than float because of conversion on line 7
print(z * 3) 