name = input("What is your name?: ") #Inputs are always strings unless converted
age = int(input("How old are you?: ")) #Wrapped int around input so that the input is converted into int after user types it in
height = float(input("How tall are you?: ")) #Wrapped float around input so it will allow decimals


print("Hello " + name)
print("You are " + str(age) + " years old") #In order to display properly, age had to converted back to str so it could be concatenated
print("You are " + str(height) + "cm tall") #similar to line 7, converts float to str this time
