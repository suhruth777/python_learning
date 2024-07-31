# Logical Operators (and,or,not) = used to check if two or more conditional staements are true

temp = int(input("What is the temperature outside?: "))
not_temp = int(input("What is the temperature outside?: "))


if temp >= 0 and temp <= 30: #both have to be true in order for print statements to run
    print('The temperature is good today!')
    print('Go outside!')
elif temp < 0 or temp > 30: #only one has to be true in order for print statement to run
    print("The temperature is bad today!")
    print("Stay inside!")



#Using not flips the requirement, if statement has to be false for prints to run
if not(not_temp >= 0 and not_temp <= 30): #both have to be false in order for print statements to run
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(not_temp < 0 or not_temp > 30): #only one has to be false in order for print statement to run
    print('The temperature is good today!')
    print('Go outside!')
