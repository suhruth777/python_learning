# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?: "))

#Order of if statements matters, even if condition is satisfied it won't print if in the wrong order.

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet")
else: #last resort
    print("You are a child!")