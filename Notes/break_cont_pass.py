# Loop Control Statements = chnage a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# Example for break
while True:
    name = input("Enter your name: ")
    if name != "":
        break
    print(name)

# Example for continue
phone_num = "609-721-5310"

for i in phone_num:
    if i == '-':
        continue
    print(i,end="")

# Example for pass
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
