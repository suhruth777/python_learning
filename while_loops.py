# while loop: A statement that will execute it's block of code, as long asit's condition remains true

# infinite loop (don't do this)
# while 1 == 1;
#     print("Help! I'm stuck in a loop")

first_name = ""
while len(first_name) == 0: #Will keep asking for input until you type something
    first_name = input("Enter your first name: ")

#or....

last_name = None

while not last_name: #Does the same thing as the first loop but uses different logic

    last_name = input("Enter your last name: ")


print("Hello, " + first_name + " " + last_name)


